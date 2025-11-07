from LuminaVisitor import LuminaVisitor
from LuminaParser import LuminaParser

class Symbol:
    def __init__(self, name, type_, value=None):
        self.name = name
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"<Symbol name={self.name}, type={self.type}, value={self.value}>"

class LuminaVisitorImpl(LuminaVisitor):
    def __init__(self):
        self.symbols = {}
        self.errors = []

    def visitDecl(self, ctx: LuminaParser.DeclContext):
        var_name = ctx.ID().getText()
        var_type = ctx.type_().getText()
        expr_value, expr_type = self.visit(ctx.expr())

        if var_name in self.symbols:
            self.errors.append(f"Erro: variável '{var_name}' já foi declarada.")
        else:
            if not self._is_type_compatible(var_type, expr_type):
                self.errors.append(
                    f"Incompatibilidade de tipos em '{var_name}': esperado {var_type}, obtido {expr_type}"
                )
            self.symbols[var_name] = Symbol(var_name, var_type, expr_value)
        return None

    def visitAssign(self, ctx: LuminaParser.AssignContext):
        var_name = ctx.ID().getText()
        expr_value, expr_type = self.visit(ctx.expr())

        if var_name not in self.symbols:
            self.errors.append(f"Erro: variável '{var_name}' não foi declarada.")
        else:
            expected_type = self.symbols[var_name].type
            if not self._is_type_compatible(expected_type, expr_type):
                self.errors.append(
                    f"Incompatibilidade de tipos em '{var_name}': esperado {expected_type}, obtido {expr_type}"
                )
            self.symbols[var_name].value = expr_value
        return None

    def visitExpr(self, ctx: LuminaParser.ExprContext):
        return self.visit(ctx.equality())

    def visitEquality(self, ctx: LuminaParser.EqualityContext):
        if len(ctx.relational()) == 1:
            return self.visit(ctx.relational(0))
        left_val, left_type = self.visit(ctx.relational(0))
        right_val, right_type = self.visit(ctx.relational(1))
        return (None, "bool")

    def visitRelational(self, ctx: LuminaParser.RelationalContext):
        if len(ctx.add()) == 1:
            return self.visit(ctx.add(0))
        return (None, "bool")

    def visitAdd(self, ctx: LuminaParser.AddContext):
        if len(ctx.mul()) == 1:
            return self.visit(ctx.mul(0))
        left_val, left_type = self.visit(ctx.mul(0))
        right_val, right_type = self.visit(ctx.mul(1))
        result_type = self._coerce_type(left_type, right_type)
        return (None, result_type)

    def visitMul(self, ctx: LuminaParser.MulContext):
        if len(ctx.unary()) == 1:
            return self.visit(ctx.unary(0))
        left_val, left_type = self.visit(ctx.unary(0))
        right_val, right_type = self.visit(ctx.unary(1))
        result_type = self._coerce_type(left_type, right_type)
        return (None, result_type)

    def visitPrimary(self, ctx: LuminaParser.PrimaryContext):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            if '.' in text:
                return (float(text), "float")
            else:
                return (int(text), "int")
        elif ctx.STRING():
            return (ctx.STRING().getText(), "text")
        elif ctx.TRUE():
            return (True, "bool")
        elif ctx.FALSE():
            return (False, "bool")
        elif ctx.ID():
            name = ctx.ID().getText()
            if name not in self.symbols:
                self.errors.append(f"Erro: variável '{name}' usada antes da declaração.")
                return (None, "erro")
            return (self.symbols[name].value, self.symbols[name].type)
        else:
            return self.visit(ctx.expr())

    def visitIoStmt(self, ctx: LuminaParser.IoStmtContext):
        if ctx.REFLECT():
            val, t = self.visit(ctx.expr())
            print(f"[reflect] {val}")
        elif ctx.INPUT():
            var_name = ctx.ID().getText()
            if var_name not in self.symbols:
                self.errors.append(f"Erro: variável '{var_name}' não foi declarada antes do input.")
            else:
                val = input(f"[input] {var_name}: ")
                self.symbols[var_name].value = val
        return None

    def _is_type_compatible(self, expected, given):
        if expected == given:
            return True
        if expected == "float" and given == "int":
            return True
        if expected == "text":
            return True
        return False

    def _coerce_type(self, t1, t2):
        if t1 == "text" or t2 == "text":
            return "text"
        if t1 == "float" or t2 == "float":
            return "float"
        if t1 == "bool" and t2 == "bool":
            return "bool"
        return "int"
