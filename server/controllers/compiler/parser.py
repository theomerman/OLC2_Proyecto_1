import ply.yacc as yacc
from controllers.compiler.lexer import tokens
from controllers.compiler.grammar.assignation import *
# from controllers.compiler.grammar.expression import *
# from controllers.compiler.grammar.tmp import *
precedence = (
    # ('left', 'OR'),
    # ('left', 'AND'),
    # ('left', 'COMPARASION', 'DIFFERENT'),
    # ('left', 'GREATER', 'LESS', 'GREATER_EQUAL', 'LESS_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'DIVIDE', 'TIMES'),
    # ('left', 'DIVIDE', 'MOD', 'TIMES'),
    # ('right', 'NOT', 'UMINUS'),
    
)



def p_init(p):
    '''init : init instruction
            | instruction'''
def p_instruction(p):
    '''instruction  : assignation
    '''
                    # | error instruction

# # declaration with type and value
# def p_assignation(p):
#     '''assignation : VAR ID COLON type EQUAL exp SEMICOLON'''
# # declaration with value
# def p_assignation2(p):
#     '''assignation : VAR ID EQUAL exp SEMICOLON'''
# # declaration with type and without value
# def p_assignation3(p):
#     '''assignation : VAR ID COLON type SEMICOLON''' 
# # types
# def p_type(p):
#     '''type : NUMBER
#             | FLOAT
#             | STRING
#             | CHAR
#             | BOOL'''

# def p_exp_number_lex(p):
#     '''exp : NUMBER_LEX'''
# def p_exp_float_lex(p):
#     '''exp : FLOAT_LEX'''
# def p_exp_string_lex(p):
#     '''exp : STRING_LEX'''
# def p_exp_char_lex(p):
#     '''exp : CHAR_LEX'''
# def p_exp_true(p):
#     '''exp : TRUE'''
# def p_exp_false(p):
#     '''exp : FALSE'''
# def p_exp_id(p):
#     '''exp : ID'''


# def p_instruction_error(p):
#     '''instruction : error SEMICOLON 
#     '''
#     print('Syntax error', p.type ,p.lineno(1))

# def p_instruction_error(p):
#     '''instruction  : NUMBER_LEX error SEMICOLON 
#     '''

def p_error(p):
    print('Syntax error', p)

parser = yacc.yacc()