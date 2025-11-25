from output.LuminaVisitor import LuminaVisitor

class LuminaSemanticVisitor(LuminaVisitor):
    def __init__(self):
        self.symbols = [{}]
        self.errors = []

    def current_scope(self):
        return self.symbols[-1]

    def push_scope(self):
        self.symbols.append({})

    def pop_scope(self):
        if len(self.symbols) > 1:
            self.symbols.pop()

    def declare_variable(self, name, var_type, ctx=None):
        scope = self.current_scope()
        if name in scope:
            self.errors.append(f"Erro: variável '{name}' já declarada neste escopo.")
        else:
            scope[name] = var_type

    def resolve_variable(self, name):
        for scope in reversed(self.symbols):
            if name in scope:
                return scope[name]
        return None

    def is_numeric(self, t):
        return t in ("int", "float")

    def is_textual(self, t):
        return t == "text"

    def is_compatible(self, left, right):
        if left is None or right is None:
            return False
        if left == right:
            return True
        if self.is_numeric(left) and self.is_numeric(right):
            return True
        return False

    def result_type(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        if self.is_textual(t1) or self.is_textual(t2):
            return "text"
        if "float" in (t1, t2):
            return "float"
        return "int"

    def log_error(self, msg):
        self.errors.append(msg)

    def visitProg(self, ctx):
        for s in ctx.stat():
            self.visit(s)

        if not self.errors:
            print("✅ Nenhum erro semântico encontrado.")
        else:
            print("\n❌ Erros semânticos encontrados:")
            for e in self.errors:
                print(" -", e)
        return None

    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        var_type = ctx.type_().getText() if ctx.type_() else None
        self.declare_variable(name, var_type, ctx)

        if ctx.expr():
            expr_type = self.visit(ctx.expr())
            if expr_type is not None and not self.is_compatible(var_type, expr_type):
                self.log_error(f"Tipos incompatíveis na declaração: '{name}' é {var_type}, recebeu {expr_type}.")
        return None

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        var_type = self.resolve_variable(name)
        if var_type is None:
            self.log_error(f"Variável '{name}' usada antes de ser declarada.")
            var_type = "int"
        expr_type = self.visit(ctx.expr())
        if expr_type is not None and not self.is_compatible(var_type, expr_type):
            self.log_error(f"Tipos incompatíveis em atribuição: '{name}' ({var_type}) recebe {expr_type}.")
        return None

    def visitReflectStat(self, ctx):
        self.visit(ctx.expr())
        return None

    def visitInputStat(self, ctx):
        name = ctx.ID().getText()
        if not self.resolve_variable(name):
            self.log_error(f"Variável '{name}' usada no input não foi declarada.")
        return None

    def visitChooseStat(self, ctx):
        cond_type = self.visit(ctx.expr())
        if cond_type and not self.is_numeric(cond_type) and not self.is_textual(cond_type):
            self.log_error("Condição de 'choose' deve ser numérica ou textual (avaliável).")
        self.push_scope()
        self.visit(ctx.block(0))
        self.pop_scope()
        if ctx.block(1):
            self.push_scope()
            self.visit(ctx.block(1))
            self.pop_scope()
        return None

    def visitWhilethinkStat(self, ctx):
        cond_type = self.visit(ctx.expr())
        if cond_type and not self.is_numeric(cond_type):
            self.log_error("Condição de 'whilethink' deve ser numérica.")
        self.push_scope()
        self.visit(ctx.block())
        self.pop_scope()
        return None

    def visitRepeatStat(self, ctx):
        self.push_scope()
        if ctx.varDecl():
            self.visit(ctx.varDecl())
        if ctx.expr():
            cond_type = self.visit(ctx.expr())
            if cond_type and not self.is_numeric(cond_type):
                self.log_error("Condição de 'repeat' deve ser numérica.")
        if ctx.assign():
            try:
                for a in ctx.assign():
                    self.visit(a)
            except TypeError:
                self.visit(ctx.assign())
        self.visit(ctx.block())
        self.pop_scope()
        return None

    def visitBlock(self, ctx):
        self.push_scope()
        for s in ctx.stat():
            self.visit(s)
        self.pop_scope()
        return None

    def visitExpr(self, ctx):
        return self.visit(ctx.logicOrExpr())

    def visitLogicOrExpr(self, ctx):
        parts = ctx.logicAndExpr()
        types = [self.visit(p) for p in parts]
        if not types:
            return None
        return "int" if len(types) > 1 else types[0]

    def visitLogicAndExpr(self, ctx):
        parts = ctx.equalityExpr()
        types = [self.visit(p) for p in parts]
        if not types:
            return None
        return "int" if len(types) > 1 else types[0]

    def visitEqualityExpr(self, ctx):
        parts = ctx.relationalExpr()
        types = [self.visit(p) for p in parts]
        if not types:
            return None
        return "int" if len(types) > 1 else types[0]

    def visitRelationalExpr(self, ctx):
        parts = ctx.additiveExpr()
        types = [self.visit(p) for p in parts]
        if not types:
            return None
        return "int" if len(types) > 1 else types[0]

    def visitAdditiveExpr(self, ctx):
        parts = ctx.multiplicativeExpr()
        types = [self.visit(p) for p in parts]
        if not types:
            return None
        result = types[0]
        for t in types[1:]:
            if not result or not t:
                result = self.result_type(result, t)
            else:
                result = self.result_type(result, t)
        return result

    def visitMultiplicativeExpr(self, ctx):
        parts = ctx.unaryExpr()
        types = [self.visit(p) for p in parts]
        if not types:
            return None
        result = types[0]
        for t in types[1:]:
            result = self.result_type(result, t)
        return result

    def visitUnaryExpr(self, ctx):
        if ctx.primaryExpr():
            return self.visit(ctx.primaryExpr())
        return None

    def visitPrimaryExpr(self, ctx):
        if ctx.NUMBER():
            txt = ctx.NUMBER().getText()
            return "float" if "." in txt else "int"
        if ctx.STRING():
            return "text"
        if ctx.ID():
            name = ctx.ID().getText()
            t = self.resolve_variable(name)
            if not t:
                self.log_error(f"Uso de variável não declarada: '{name}'.")
                return None
            return t
        if ctx.expr():
            return self.visit(ctx.expr())
        return None
