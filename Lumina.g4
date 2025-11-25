grammar Lumina;

// Regras Sintáticas

prog: stat+ EOF;

stat
    : varDecl
    | assign
    | reflectStat
    | inputStat
    | chooseStat
    | repeatStat
    | whilethinkStat
    | block
    ;

varDecl
    : DEFINE ID COLON type (ASSIGN expr)? SEMI
    ;

assign
    : ID ASSIGN expr SEMI
    ;

reflectStat
    : REFLECT expr SEMI
    ;

inputStat
    : INPUT ID SEMI
    ;

chooseStat
    : CHOOSE LPAREN expr RPAREN PATH block (OR block)?
    ;

repeatStat
    : REPEAT LPAREN varDecl expr SEMI assign RPAREN block
    ;

whilethinkStat
    : WHILETHINK LPAREN expr RPAREN block
    ;

block
    : LBRACE stat* RBRACE
    ;

// Expressões

expr
    : logicOrExpr
    ;

logicOrExpr
    : logicAndExpr (OR logicAndExpr)*
    ;

logicAndExpr
    : equalityExpr (AND equalityExpr)*
    ;

equalityExpr
    : relationalExpr ((EQ | NEQ) relationalExpr)*
    ;

relationalExpr
    : additiveExpr ((LT | GT | LE | GE) additiveExpr)*
    ;

additiveExpr
    : multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*
    ;

multiplicativeExpr
    : unaryExpr ((STAR | DIV) unaryExpr)*
    ;

unaryExpr
    : (NOT | PLUS | MINUS)? primaryExpr
    ;

primaryExpr
    : NUMBER
    | STRING
    | ID
    | LPAREN expr RPAREN
    ;

// Tipos

type
    : INT
    | FLOAT
    | TEXT
    ;

// Léxico

// Palavras reservadas
DEFINE      : 'define';
REFLECT     : 'reflect';
INPUT       : 'input';
CHOOSE      : 'choose';
PATH        : 'path';
OR          : 'or';
AND         : 'and';
NOT         : 'not';
REPEAT      : 'repeat';
WHILETHINK  : 'whilethink';
RETURN      : 'return';
TRUE        : 'true';
FALSE       : 'false';

// Tipos
INT         : 'int';
FLOAT       : 'float';
TEXT        : 'text';

// Símbolos e operadores
PLUS    : '+';
MINUS   : '-';
STAR    : '*';
DIV     : '/';
ASSIGN  : '=';
COLON   : ':';
LT      : '<';
GT      : '>';
LE      : '<=';
GE      : '>=';
EQ      : '==';
NEQ     : '!=';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
SEMI    : ';';
COMMA   : ',';

// Literais e IDs
NUMBER  : [0-9]+ ('.' [0-9]+)?;
STRING  : '"' (~["\\\r\n] | '\\' .)* '"';
ID      : [a-zA-Z_][a-zA-Z0-9_]*;

// Comentários e espaços
COMMENT : '#' ~[\r\n]* -> skip;
WS      : [ \t\r\n]+ -> skip;