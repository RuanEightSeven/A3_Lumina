from antlr4 import *
from output.LuminaLexer import LuminaLexer
from output.LuminaParser import LuminaParser
from semantic import LuminaSemanticVisitor
from semantic.LuminaErrorListener import LuminaErrorListener

def main():
    # input_stream = FileStream("examples/teste1_valido.lumina", encoding="utf-8")
    # input_stream = FileStream("examples/teste2_repeticoes.lumina", encoding="utf-8")
    # input_stream = FileStream("examples/teste3_erros_semanticos.lumina", encoding="utf-8")
    # input_stream = FileStream("examples/teste4_erros_sintaticos.lumina", encoding="utf-8")
    # input_stream = FileStream("examples/teste5_aninhamentos.lumina", encoding="utf-8")
    # input_stream = FileStream("examples/teste6_operadores_logicos.lumina", encoding="utf-8")
    # input_stream = FileStream("examples/projeto1_simulacao_clareza.lumina", encoding="utf-8")
    input_stream = FileStream("examples/projeto2_medidor_produtividade.lumina", encoding="utf-8")
    # input_stream = FileStream("examples/projeto3_processamento_ideias.lumina", encoding="utf-8")
    # input_stream = FileStream("examples/projeto4_modelo_tomada_decisao.lumina", encoding="utf-8")

    lexer = LuminaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = LuminaParser(stream)

    # Adicionamos um listener customizado para ouvir erros sintáticos (isso não estava acontecendo com o padrão, apenas gerando uma stacktrace error)
    parser.removeErrorListeners()
    error_listener = LuminaErrorListener()
    parser.addErrorListener(error_listener)

    tree = parser.prog()

    print("Arvere Sintática basica")
    print(tree.toStringTree(recog=parser))

    if error_listener.has_errors():
        error_listener.report()
        print("\n⚠️ Análise semântica não executada devido a erros de sintaxe.")
        return

    print("Visitor")
    visitor = LuminaSemanticVisitor.LuminaSemanticVisitor()
    visitor.visit(tree)

    print("\nTabela de símbolos:")
    for i, scope in enumerate(visitor.symbols):
        print(f" Escopo {i}:")
        for name, vtype in scope.items():
            print(f"   {name} : {vtype}")

    if visitor.errors:
        print("\n❌ Código não compilado devido a erros semânticos.")
    else:
        print("\n✅ Código compilado com sucesso!")

if __name__ == "__main__":
    main()
