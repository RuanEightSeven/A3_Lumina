Lumina - README
===============

Conteúdo do pacote
------------------
- alfabeto.txt         : descrição do alfabeto, tokens e símbolos.
- gramatica.txt        : gramática LL(1) em nível alto (explicativa).
- Lumina.g4            : gramática ANTLR (lexer + parser).
- exemplo.lumina       : exemplo de programa escrito em Lumina.
- mini_instrucoes.txt  : instruções rápidas para implementação/compilação.

Guia rápido para o compilador (sugestões de implementação)
---------------------------------------------------------
1. Ferramenta recomendada: ANTLR v4.
   - Gere parser e lexer a partir de Lumina.g4.
   - Implemente um visitor ou listener para análise semântica e geração de código.

2. Etapas do compilador:
   - Tokenização/Lexing (ANTLR)
   - Parsing (ANTLR -> árvore sintática)
   - Análise semântica:
       * Tabela de símbolos (scopes simples por blocos)
       * Verificação de declaração prévia e tipos nas atribuições e expressões
       * Coerção de tipos (ex.: int -> float) onde aplicável, sinalizando conversões
       * Verificação de retorno de funções (se implementado)
   - Geração de código intermediário (opcional) ou saída para C/Java.
   - Mensagens de erro claras (linha:coluna)

3. Tipos e regras de coerção (sugestão):
   - int x int -> int
   - int x float -> float (conversão automática do int para float)
   - text concatenation: text + any -> text (concatenação via toString)
   - Comparações: permitidas entre tipos compatíveis (ex.: int e float)

4. Funções extras (diferenciais):
   - Inferência de tipo em expressões literais
   - Otimizações simples (folding de expressões constantes)
   - Warnings para variáveis não usadas

Exemplo de como compilar com ANTLR (linha de comando)
---------------------------------------------------
1) Gerar código Java (supondo ANTLR4 jar disponível):
   java -jar antlr-4.x-complete.jar Lumina.g4
2) Compilar as classes Java geradas:
   javac *.java
3) Executar analisador com um runner que você implemente (Main.java)

Observações finais
------------------
- A gramática Lumina.g4 foi projetada para facilitar a análise de precedência de operadores
  e evitar recursividade à esquerda. Ajustes finos podem ser necessários de acordo com
  requisitos do time e do projeto de compilador.
