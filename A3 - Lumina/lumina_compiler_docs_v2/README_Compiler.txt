Lumina Compiler Visitor
=======================

Este pacote contém a implementação do visitor semântico da linguagem Lumina.

Arquivos incluídos:
- LuminaVisitorImpl.py  → implementação do visitor (checagem de tipos, tabela de símbolos, IO)
- main.py               → script principal para rodar o compilador
- README_Compiler.txt   → instruções de uso

Como usar:
-----------
1. Gere o parser e lexer com ANTLR:
   antlr4 -Dlanguage=Python3 Lumina.g4

2. Compile o código Python (já pronto).
3. Execute o compilador com:
   python main.py exemplo.lumina

O visitor faz:
---------------
- Registro de variáveis na tabela de símbolos;
- Verificação de tipos e compatibilidade;
- Emissão de erros semânticos;
- Execução simbólica dos comandos reflect/input;
- Impressão de resultados e tabela final.
