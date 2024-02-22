# ------------------------------------------------------------
# calclex.py
import ply.lex as lex

# List of token names.   This is always required
tokens = [
   'ID',
   'COMMENT',
   'COMMENT2',
   'NUMBER_LEX',
   'FLOAT_LEX',
   'STRING_LEX',
   'CHAR_LEX',

    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'DOT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',


    'COMPARASION',
    'EQUALS',
    'DIFFERENT',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',

    'AND',
    'OR',
    'NOT',


]

reserved = {
    'null': 'NULL',
    'true': 'TRUE',
    'false': 'FALSE',
    'var': 'VAR',
    'const': 'CONST',
    
    'number': 'NUMBER',
    'string': 'STRING',
    'float': 'FLOAT',
    'char': 'CHAR',

    'function': 'FUNCTION',

    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',

    'if': 'IF',
    'else': 'ELSE',

    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    
    'while': 'WHILE',

    'for': 'FOR',
    'of': 'OF',

}


tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_SEMICOLON  = r'\;'
t_COLON = r'\:'
t_COMMA  = r'\,'
t_DOT  = r'\.'
t_PLUS  = r'\+'
t_MINUS  = r'\-'
t_TIMES  = r'\*'
t_DIVIDE  = r'\/'
t_MOD = r'\%'

t_COMPARASION = r'\=\='
t_EQUALS = r'\='
t_DIFFERENT = r'\!\='
t_GREATER = r'\>'
t_LESS = r'\<'
t_GREATER_EQUAL = r'\>\='
t_LESS_EQUAL = r'\<\='

t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

t_TERNARY = r'\?\:'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

def t_COMMENT(t):
    r'\/\/.*'
    pass
def t_COMMENT2(t):
    r'\/\*[\s\S]*?\*\/'
    pass

# A regular expression rule with some action code
def t_NUMBER_LEX(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT_LEX(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING_LEX(t):
    r'\".*\"'
    t.type = reserved.get(t.value, 'STRING')    # Check for reserved words
    return t

def t_char_LEX(t):
    r'\'[a-zA-Z0-9]\''
    t.type = reserved.get(t.value, 'CHAR')    # Check for reserved words
    return t



























# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
3
"hello"
true
hello
'''


# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
