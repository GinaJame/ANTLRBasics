// concrete syntax
grammar ginaTarea;

program:
    statem*
    | expr*;


statem:
    ID ' =' expr  #AsignExpression
    | ID ' = "' STRING '"'  #Asign
    | 'if (' cond=expr ') then {' instruc=expr '} else {' instruc2=expr '}' #ifElse
    | 'if (' cond=expr ') then {' instruc=expr '}'  #if
    | tipo=('int' | 'bool') ID #declaracion
    | tipo=('String' | 'float') ID #declaracion
;
// non-terminals expressed as context-free grammar (BNF)
expr:	left=expr op=('*'|'/') right=expr  # Aritmetica
    |	left=expr op=('+'|'-') right=expr  # Aritmetica
    |   left=expr op=('>'|'<') right=expr #Logica
    |   left=expr op=('>='|'<=') right=expr #Logica
    |   left=expr op=('&'|'|') right=expr #Logica
    |	atom=INT                           # Atomo
    |	'(' expr ')'                       # Parentesis
    | 'print(' expr ')'    #Print
    | 'print( ' STRING ' )'     #PrintString
    ;

// tokens expressed as regular expressions
INT : [0-9]+ ;
WS  :   [ \t]+ -> skip ;
ID: [a-z][_a-zA-Z0-9]* ;
STRING: [_a-zA-Z0-9]*[_a-zA-Z0-9]* ;

