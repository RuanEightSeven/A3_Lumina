from antlr4 import *
from output.LuminaLexer import LuminaLexer
from output.LuminaParser import LuminaParser
from output.LuminaVisitor import LuminaVisitor
from semantic import LuminaSemanticVisitor

def main():
    # Lê o código da linguagem (arquivo de exemplo)
    input_stream = FileStream("examples/teste1.txt", encoding="utf-8")
    
    # Etapa 1: Lexer (transforma o texto em tokens)
    lexer = LuminaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Etapa 2: Parser (monta a estrutura da linguagem)
    parser = LuminaParser(stream)
    tree = parser.prog()  # 'prog' é a regra inicial da gramática

    # Exibe a árvore sintática resultante
    print("Arvere Sintática basica")
    print(tree.toStringTree(recog=parser))

    # Visitor semantico
    print("Visitor")
    visitor = LuminaSemanticVisitor.LuminaSemanticVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()
