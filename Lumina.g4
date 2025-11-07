grammar Lumina;
// Ref de organização dos blocos: https://tomassetti.me/antlr-mega-tutorial/

// Diário de alterações
// 04/11 - alterado para respeitar precedencia
// 06/11 - incluir nas expressões '==' pro if, while e for e consertando a formatação errada(kkkk) e depois da definição dos nomes dos tokens, alterei pra utilizar o nome nas expressões

//===============================
//  Bloco sintatico  - Parser
//===============================

prog: stat+ ;

stat
    : assign
    | decl
    | ifStat
    | whileStat
    | forStat
    | printStat
    | readStat
    | block
    ;

assign : ID ASSIGN expr SEMI ;

expr        : orExpr ;

orExpr      : andExpr (OR andExpr)* ;
andExpr     : eqExpr  (AND eqExpr)* ;
eqExpr      : relExpr ( (EQ | NEQ) relExpr )* ;
relExpr     : somaExpr ( (LT | LE | GT | GE) somaExpr )* ;
somaExpr    : termo ( (PLUS | MINUS) termo )* ;
termo       : fator ( (MULT | DIV) fator )* ;
fator       : (PLUS | MINUS)? (NUMBER | ID | LPAREN expr RPAREN) ;

// Tipo e Declaração
decl : tipo ID (ASSIGN expr)? SEMI ;
tipo : INT_TYPE | FLOAT_TYPE | STRING_TYPE ;

// Controle
ifStat     : IF LPAREN expr RPAREN stat (ELSE stat)? ;
whileStat  : WHILE LPAREN expr RPAREN stat ;
forStat    : FOR LPAREN assign expr SEMI assign RPAREN stat ;
block      : LBRACE stat* RBRACE ;

// Input e Output
printStat  : PRINTF LPAREN STRING (COMMA expr)* RPAREN SEMI ;
readStat   : SCANF  LPAREN STRING (COMMA ID)* RPAREN SEMI ;

//===============================
//  Bloco Lexico  - Lexer
//===============================

// Tipos (Três tipos de variáveis)
INT_TYPE    : 'int' ;
FLOAT_TYPE  : 'float' ;
STRING_TYPE : 'string' ;

// Controle
IF    : 'if' ;
ELSE  : 'else' ;
WHILE : 'while' ;
DO    : 'do' ;
FOR   : 'for' ;

// Input e Output
PRINTF : 'printf' ;
SCANF  : 'scanf' ;

// Literais
NUMBER : [0-9]+ ('.' [0-9]+)? ;
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
STRING : '"' (~["\\] | '\\' .)* '"' ;

// Operadores
PLUS   : '+' ;
MINUS  : '-' ;
MULT   : '*' ;
DIV    : '/' ;
GT     : '>' ;
GE     : '>=' ;
LT     : '<' ;
LE     : '<=' ;
EQ     : '==' ;
NEQ    : '!=' ;
AND    : '&&' ;
OR     : '||' ;
ASSIGN : '=' ;

// Separadores
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
SEMI   : ';' ;
COMMA  : ',' ;

// Recursão
WS : [ \t\r\n]+ -> skip ;

// Comentários de linha e bloco
LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
