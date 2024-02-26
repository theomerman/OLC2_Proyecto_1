# from controllers.compiler.grammar.expression import *
# # declaration with type and value
# def p_assignation(p):
#     '''assignation : VAR ID COLON type EQUAL exp SEMICOLON'''
# # declaration with value
# def p_assignation2(p):
#     '''assignation : VAR ID EQUAL exp SEMICOLON'''
# # declaration with type and without value
# def p_assignation3(p):
#     '''assignation : VAR ID COLON type SEMICOLON''' 
# types
# def p_type(p):
#     '''type : NUMBER
#             | FLOAT
#             | STRING
#             | CHAR
#             | BOOL'''

def p_assignation(p):
    '''assignation : VAR ID COLON type EQUAL  SEMICOLON
    '''
# types
def p_type(p):
    '''type : NUMBER
            | FLOAT
            | STRING
            | CHAR
            | BOOL'''


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