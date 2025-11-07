from output.LuminaVisitor import LuminaVisitor


class LuminaSemanticVisitor(LuminaVisitor):
    def __init__(self):
        super().__init__()
        self.tabela_simbolos = {}  # {nome: tipo}

    # Visita declarações de variáveis
    def visitDecl(self, ctx):
        tipo = ctx.tipo().getText()
        nome = ctx.ID().getText()

        if nome in self.tabela_simbolos:
            print(f"Erro: variável '{nome}' já declarada.")
        else:
            self.tabela_simbolos[nome] = tipo
            print(f"Declaração: {tipo} {nome}")

        return self.visitChildren(ctx)

    # Visita atribuições
    def visitAssign(self, ctx):
        nome = ctx.ID().getText()
        if nome not in self.tabela_simbolos:
            print(f"Erro: variável '{nome}' não foi declarada.")
        else:
            print(f"Atribuição em: {nome}")

        return self.visitChildren(ctx)

    # Visita expressões (opcional — debug)
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)
    
    # Apos alteracao de int e float pra number
    def visitFator(self, ctx):
        if ctx.ID():
            var = ctx.ID().getText()
            if var not in self.tabela_simbolos:
                print(f"Erro: variável '{var}' não foi declarada.")
            else:
                print(f"Uso da variável: {var}")
        return self.visitChildren(ctx)

