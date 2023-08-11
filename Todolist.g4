grammar Todolist;

KEYWORDS: 'tarefa' | 'descricao' | 'data' | 'status';
NUMERO: [0-9];
WHITE_SPACE: ([ \t\r\n]) -> skip;
CADEIA: '"' ~('"'|'\r'|'\n')* '"';
DATA: NUMERO NUMERO '/' NUMERO NUMERO '/' NUMERO NUMERO;
STATUS: 'feito' | 'a fazer';

tarefa:
    'tarefa:' CADEIA 'descricao:' CADEIA 'data:' DATA 'status:' STATUS;