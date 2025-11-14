# semantic/LuminaCodeGenVisitor.py
from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNode
from output.LuminaVisitor import LuminaVisitor

class LuminaCodeGenVisitor(LuminaVisitor):
    """
    Gera código Java a partir da AST de Lumina.
    - Integra com a tabela de símbolos do visitor semântico.
    - Gera leitura 'input' tipada automaticamente (nextInt, nextDouble, nextLine).
    - Produz uma classe Java chamada LuminaProgram com método main.
    """

    def __init__(self, symbol_table_stack=None, target="Java"):
        assert target == "Java", "Atualmente só suportamos Java."
        self.target = target

        self.symbol_table_stack = symbol_table_stack or [{}]

        self.lines = []
        self.top_lines = []
        self.indent_level = 2
        self.needs_scanner = False

    # --------------------------
    # helpers de geração
    # --------------------------
    def emit(self, line=""):
        self.lines.append(" " * (self.indent_level * 4) + line)

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1

    def get_code(self):
        code = []
        if self.needs_scanner:
            code.append("import java.util.Scanner;")
            code.append("")
        code.append("public class LuminaProgram {")
        code.append("    public static void main(String[] args) {")
        if self.needs_scanner:
            code.append("        Scanner __sc = new Scanner(System.in);")

        code.extend(self.lines)

        if self.needs_scanner:
            code.append("        __sc.close();")
        code.append("    }")
        code.append("}")
        return "\n".join(code)

    def map_type(self, lumina_type):
        t = lumina_type.lower()
        if t == "int":
            return "int"
        if t == "float":
            return "double"
        if t == "text":
            return "String"
        return "Object"

    # --------------------------
    # VISITORS principais
    # --------------------------
    def visitProg(self, ctx):
        for s in ctx.stat():
            self.visit(s)
        return None

    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        lum_type = ctx.type_().getText() if ctx.type_() else "int"
        jtype = self.map_type(lum_type)
        expr_code = self.visit(ctx.expr()) if ctx.expr() else None
        if expr_code:
            self.emit(f"{jtype} {name} = {expr_code};")
        else:
            self.emit(f"{jtype} {name};")
        return None

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        expr_code = self.visit(ctx.expr())
        self.emit(f"{name} = {expr_code};")
        return None

    def visitReflectStat(self, ctx):
        expr_code = self.visit(ctx.expr())
        self.emit(f"System.out.println({expr_code});")
        return None

    def visitInputStat(self, ctx):
        name = ctx.ID().getText()
        self.needs_scanner = True

        # encontra tipo na tabela de símbolos
        var_type = self.lookup_type(name)
        if var_type == "int":
            method = "__sc.nextInt()"
        elif var_type == "float":
            method = "__sc.nextDouble()"
        else:
            method = "__sc.nextLine()"

        self.emit(f"{name} = {method};")
        return None

    def lookup_type(self, name):
        # busca o tipo na pilha de escopos
        for scope in reversed(self.symbol_table_stack):
            if name in scope:
                return scope[name]
        return None

    def visitChooseStat(self, ctx):
        cond = self.visit(ctx.expr())
        self.emit(f"if ({cond}) {{")
        self.indent()
        self.visit(ctx.block(0))
        self.dedent()
        if ctx.block(1):
            self.emit("} else {")
            self.indent()
            self.visit(ctx.block(1))
            self.dedent()
        self.emit("}")
        return None

    def visitRepeatStat(self, ctx):
        init = self.varDecl_inline(ctx.varDecl()) if ctx.varDecl() else ""
        cond = self.visit(ctx.expr()) if ctx.expr() else ""
        incr = self.assign_inline(ctx.assign()) if ctx.assign() else ""
        self.emit(f"for ({init}; {cond}; {incr}) {{")
        self.indent()
        self.visit(ctx.block())
        self.dedent()
        self.emit("}")
        return None

    def visitWhilethinkStat(self, ctx):
        cond = self.visit(ctx.expr())
        self.emit(f"while ({cond}) {{")
        self.indent()
        self.visit(ctx.block())
        self.dedent()
        self.emit("}")
        return None

    def visitBlock(self, ctx):
        self.emit("{")
        self.indent()
        for s in ctx.stat():
            self.visit(s)
        self.dedent()
        self.emit("}")
        return None

    # inline helpers
    def varDecl_inline(self, ctx):
        name = ctx.ID().getText()
        lum_type = ctx.type_().getText() if ctx.type_() else "int"
        jtype = self.map_type(lum_type)
        expr_code = self.visit(ctx.expr()) if ctx.expr() else None
        if expr_code:
            return f"{jtype} {name} = {expr_code}"
        return f"{jtype} {name}"

    def assign_inline(self, ctx):
        name = ctx.ID().getText()
        expr_code = self.visit(ctx.expr())
        return f"{name} = {expr_code}"

    # --------------------------
    # EXPRESSÕES
    # --------------------------
    def visitExpr(self, ctx): return self.visit(ctx.logicOrExpr())
    def visitLogicOrExpr(self, ctx):
        parts = [self.visit(e) for e in ctx.logicAndExpr()]
        return " || ".join(parts)
    def visitLogicAndExpr(self, ctx):
        parts = [self.visit(e) for e in ctx.equalityExpr()]
        return " && ".join(parts)
    def visitEqualityExpr(self, ctx):
        if len(ctx.relationalExpr()) == 1:
            return self.visit(ctx.relationalExpr(0))
        return self._join_children_text(ctx)
    def visitRelationalExpr(self, ctx):
        if len(ctx.additiveExpr()) == 1:
            return self.visit(ctx.additiveExpr(0))
        return self._join_children_text(ctx)
    def visitAdditiveExpr(self, ctx):
        if len(ctx.multiplicativeExpr()) == 1:
            return self.visit(ctx.multiplicativeExpr(0))
        return self._join_children_text(ctx)
    def visitMultiplicativeExpr(self, ctx):
        if len(ctx.unaryExpr()) == 1:
            return self.visit(ctx.unaryExpr(0))
        return self._join_children_text(ctx)
    def visitUnaryExpr(self, ctx):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            val = self.visit(ctx.primaryExpr())
            if op == "not":
                return f"!({val})"
            return f"{op}{val}"
        return self.visit(ctx.primaryExpr())
    def visitPrimaryExpr(self, ctx):
        if ctx.NUMBER(): return ctx.NUMBER().getText()
        if ctx.STRING(): return ctx.STRING().getText()
        if ctx.ID(): return ctx.ID().getText()
        if ctx.expr(): return f"({self.visit(ctx.expr())})"
        return ""
    def _join_children_text(self, ctx):
        out = []
        for c in ctx.getChildren():
            if isinstance(c, ParserRuleContext):
                out.append(self.visit(c))
            else:
                txt = c.getText()
                if txt == "and": txt = "&&"
                elif txt == "or": txt = "||"
                elif txt == "not": txt = "!"
                out.append(txt)
        return " ".join(out)
