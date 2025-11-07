import sys
from antlr4 import *
from LuminaLexer import LuminaLexer
from LuminaParser import LuminaParser
from LuminaVisitorImpl import LuminaVisitorImpl

def main(filename):
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = LuminaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LuminaParser(stream)
    tree = parser.program()

    visitor = LuminaVisitorImpl()
    visitor.visit(tree)

    print("\nTabela de símbolos:")
    for sym in visitor.symbols.values():
        print(sym)

    if visitor.errors:
        print("\nErros semânticos:")
        for e in visitor.errors:
            print(" -", e)
    else:
        print("\nCompilação bem-sucedida! 🌟")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.lumina>")
    else:
        main(sys.argv[1])
