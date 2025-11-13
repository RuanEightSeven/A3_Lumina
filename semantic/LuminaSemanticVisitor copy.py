from output.LuminaVisitor import LuminaVisitor

class LuminaSemanticVisitor(LuminaVisitor):
    """
    Visitor semântico compatível com a gramática Lumina.g4.
    Implementa:
      - Verificação de declarações duplicadas;
      - Uso de variáveis não declaradas;
      - Checagem básica de tipos (int, float, string);
      - Controle de escopos;
      - Relato de erros ao final da execução.
    """

    def __init__(self):
        self.symbol_table_stack = [{}]  # pilha de escopos (para if, while, for, blocos)
        self.errors = []

    # ---------------------------------------------------------
    # Utilitários internos
    # ---------------------------------------------------------
    def current_scope(self):
        return self.symbol_table_stack[-1]

    def push_scope(self):
        self.symbol_table_stack.append({})

    def pop_scope(self):
        self.symbol_table_stack.pop()

    def declare_variable(self, name, var_type):
        scope = self.current_scope()
        if name in scope:
            self.errors.append(f"Erro: variável '{name}' já declarada neste escopo.")
        else:
            scope[name] = var_type

    def resolve_variable(self, name):
        for scope in reversed(self.symbol_table_stack):
            if name in scope:
                return scope[name]
        return None

    def is_numeric(self, t):
        return t in ["int", "float"]

    def is_compatible(self, t1, t2):
        if t1 == t2:
            return True
        if self.is_numeric(t1) and self.is_numeric(t2):
            return True
        return False

    def result_type(self, t1, t2):
        if "float" in (t1, t2):
            return "float"
        return "int"

    def log_error(self, msg):
        self.errors.append(msg)

    # ---------------------------------------------------------
    # Visitadores principais
    # ---------------------------------------------------------
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

    # -----------------------------
    # Declaração de variável
    # -----------------------------
    def visitDecl(self, ctx):
        var_type = ctx.tipo().getText()
        var_name = ctx.ID().getText()
        self.declare_variable(var_name, var_type)

        if ctx.expr():
            expr_type = self.visit(ctx.expr())
            if expr_type and not self.is_compatible(var_type, expr_type):
                self.log_error(
                    f"Tipos incompatíveis na declaração: '{var_name}' é {var_type}, mas recebeu {expr_type}."
                )
        return None

    # -----------------------------
    # Atribuição
    # -----------------------------
    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        var_type = self.resolve_variable(var_name)
        if not var_type:
            self.log_error(f"Variável '{var_name}' usada antes de ser declarada.")
            var_type = "int"  # assume tipo neutro para continuar análise

        expr_type = self.visit(ctx.expr())
        if expr_type and not self.is_compatible(var_type, expr_type):
            self.log_error(
                f"Tipos incompatíveis em atribuição: '{var_name}' é {var_type}, mas recebeu {expr_type}."
            )
        return None

    # -----------------------------
    # Estruturas de controle
    # -----------------------------
    def visitIfStat(self, ctx):
        cond_type = self.visit(ctx.expr())
        if cond_type and not self.is_numeric(cond_type):
            self.log_error("Condição do 'if' deve ser numérica.")
        self.push_scope()
        self.visit(ctx.stat(0))
        self.pop_scope()
        if ctx.stat(1):
            self.push_scope()
            self.visit(ctx.stat(1))
            self.pop_scope()
        return None

    def visitWhileStat(self, ctx):
        cond_type = self.visit(ctx.expr())
        if cond_type and not self.is_numeric(cond_type):
            self.log_error("Condição do 'while' deve ser numérica.")
        self.push_scope()
        self.visit(ctx.stat())
        self.pop_scope()
        return None

    def visitForStat(self, ctx):
        self.push_scope()
        self.visit(ctx.assign(0))  # inicialização
        cond_type = self.visit(ctx.expr())
        if cond_type and not self.is_numeric(cond_type):
            self.log_error("Condição do 'for' deve ser numérica.")
        self.visit(ctx.assign(1))  # incremento
        self.visit(ctx.stat())
        self.pop_scope()
        return None

    # -----------------------------
    # Leitura e impressão
    # -----------------------------
    def visitPrintStat(self, ctx):
        for e in ctx.expr():
            self.visit(e)
        return None

    def visitReadStat(self, ctx):
        for id_node in ctx.ID():
            var_name = id_node.getText()
            if not self.resolve_variable(var_name):
                self.log_error(f"Variável '{var_name}' usada em scanf não foi declarada.")
        return None

    # -----------------------------
    # Blocos
    # -----------------------------
    def visitBlock(self, ctx):
        self.push_scope()
        for s in ctx.stat():
            self.visit(s)
        self.pop_scope()
        return None

    # -----------------------------
    # Expressões (expr, termo, fator)
    # -----------------------------
    def visitExpr(self, ctx):
        termo_types = [self.visit(t) for t in ctx.termo()]
        if not termo_types:
            return None
        result_type = termo_types[0]
        for t in termo_types[1:]:
            if not self.is_numeric(result_type) or not self.is_numeric(t):
                self.log_error(f"Operação inválida entre {result_type} e {t}.")
            result_type = self.result_type(result_type, t)
        return result_type

    def visitTermo(self, ctx):
        fator_types = [self.visit(f) for f in ctx.fator()]
        if not fator_types:
            return None
        result_type = fator_types[0]
        for t in fator_types[1:]:
            if not self.is_numeric(result_type) or not self.is_numeric(t):
                self.log_error(f"Operação inválida entre {result_type} e {t}.")
            result_type = self.result_type(result_type, t)
        return result_type

    def visitFator(self, ctx):
        if ctx.NUMBER():
            txt = ctx.NUMBER().getText()
            return "float" if "." in txt else "int"
        elif ctx.ID():
            var_name = ctx.ID().getText()
            var_type = self.resolve_variable(var_name)
            if not var_type:
                self.log_error(f"Variável '{var_name}' usada antes de ser declarada.")
                return None
            return var_type
        elif ctx.expr():
            return self.visit(ctx.expr())
        return None
