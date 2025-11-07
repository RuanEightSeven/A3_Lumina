grammar Lumina;

// ---------- Parser rules ----------
program
    : decl* stmt* EOF
    ;

decl
    : DEFINE ID ':' type '=' expr ';'
    ;

type
    : 'int'
    | 'float'
    | 'text'
    | 'bool'
    ;

stmt
    : exprStmt
    | ioStmt
    | ifStmt
    | forStmt
    | whileStmt
    | returnStmt
    ;

exprStmt
    : expr ';'
    ;

ioStmt
    : REFLECT expr ';'
    | INPUT ID ';'
    ;

ifStmt
    : CHOOSE '(' expr ')' PATH block ( OR block )?
    ;

forStmt
    : REPEAT '(' (decl | assign) ';' expr ';' assign ')' block
    ;

whileStmt
    : WHILETHINK '(' expr ')' block
    ;

returnStmt
    : RETURN expr ';'
    ;

assign
    : ID '=' expr
    ;

block
    : '{' stmt* '}'
    ;

// Expressions with precedence
expr
    : equality
    ;

equality
    : relational ( (EQ | NEQ) relational )*
    ;

relational
    : add ( ('<' | '>' | LEQ | GEQ) add )*
    ;

add
    : mul ( ('+' | '-') mul )*
    ;

mul
    : unary ( ('*' | '/') unary )*
    ;

unary
    : ('-' | NOT) unary
    | primary
    ;

primary
    : NUMBER
    | STRING
    | ID
    | '(' expr ')'
    | TRUE
    | FALSE
    ;

// ---------- Lexer rules ----------
DEFINE: 'define';
REFLECT: 'reflect';
INPUT: 'input';
CHOOSE: 'choose';
PATH: 'path';
OR: 'or';
REPEAT: 'repeat';
WHILETHINK: 'whilethink';
RETURN: 'return';

TRUE: 'true';
FALSE: 'false';

NOT: 'not';

EQ: '==';
NEQ: '!=';
LEQ: '<=';
GEQ: '>=';

ID: [a-zA-Z_] [a-zA-Z_0-9]* ;

NUMBER
    : DIGIT+ ('.' DIGIT+)?
    ;

STRING
    : '"' ( ~["\\] | '\\' . )* '"'
    ;

COMMENT: '#' ~[\r\n]* -> skip ;

WS: [ \t\r\n]+ -> skip ;

// fragments
fragment DIGIT: [0-9] ;
