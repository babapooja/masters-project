
# -----------------------------------------------------------------------------
#
#
#
# -----------------------------------------------------------------------------

import ply.lex as lex
reserved = {
    'for': 'FOR',
    'in': 'IN',
    'where': 'WHERE',
    'return': 'RETURN',
}

tokens = [
    'NAME', 'DOT', 'LBRACKET', 'RBRACKET', 'LPAREN', 'RPAREN', 'STRING',
    'NUMBER', 'COMMA', 'JSONLINES', 'VARIABLE',  'FILENAME', "INVERTEDCOMMA", "LCBRACKET", "RCBRACKET", "COLON"
] + list(reserved.values())


# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'  # eg: john
t_STRING = r'\"[a-zA-Z_][a-zA-Z0-9_]*"'  # eg: 'john' or "john"
t_FILENAME = r"[a-zA-Z_][a-zA-Z0-9-_]*.json"  # eg: 'abc.json'
t_VARIABLE = r'\$[a-zA-Z_][a-zA-Z0-9_]*'
t_DOT = r'\.'
t_COLON = r'\:'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
t_COMMA = r'\,'
t_INVERTEDCOMMA = r'["\']'
t_ignore_COMMENT = r'\#.*'


def t_JSONLINES(t):
    r'json-lines'
    t.value = 'json-lines'
    return t


def t_FOR(t):
    r'[fF][oO][rR]'
    t.value = 'for'
    return t


def t_IN(t):
    r'[iI][nN]'
    t.value = 'in'
    return t


def t_WHERE(t):
    r'[wW][hH][eE][rR][eE]'
    t.value = 'where'
    return t


def t_RETURN(t):
    r'[rR][eE][tT][uU][rR][nN]'
    t.value = 'return'
    return t


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


t_ignore = " \r\n\t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# lexer.input(inputdata)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)