import ply.yacc as yacc
from controllers.compiler.lexer import tokens
def p_init(p):
    '''init : init instruction
            | instruction'''
def p_instruction(p):
    '''instruction  : NUMBER_LEX STRING_LEX SEMICOLON 
    '''