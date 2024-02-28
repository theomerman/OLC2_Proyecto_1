import ply.yacc as yacc
from controllers.compiler.lexer import tokens
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'COMPARASION', 'DIFFERENT'),
    ('left', 'GREATER', 'LESS', 'GREATER_EQUAL', 'LESS_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'DIVIDE', 'MOD', 'TIMES'),
    ('right', 'UNOT', 'UMINUS'),
    
)



def p_init(p):
    '''init : init instruction
            | empty
            | instruction'''

def p_instruction(p):
    '''instruction  : assignation SEMICOLON
                    | assignation_const SEMICOLON
                    | interface
                    | if
                    | while
                    | for
                    | foreach
                    | break
                    | continue
                    | return
    '''
#######################################################################
# if
def p_if(p):
    '''if : IF LPAREN exp RPAREN block
          | IF LPAREN exp RPAREN block ELSE block
          | IF LPAREN exp RPAREN block ELSE if'''
#######################################################################
# while
def p_while(p):
    '''while : WHILE LPAREN exp RPAREN block'''
#######################################################################
# for
def p_for(p):
    '''for : FOR LPAREN assignation SEMICOLON exp SEMICOLON assignation RPAREN block'''
#######################################################################
# for each
def p_foreach(p):
    '''foreach : FOR LPAREN VAR ID OF ID RPAREN block'''
#######################################################################
# break
def p_break(p):
    '''break : BREAK SEMICOLON'''
#######################################################################
# continue
def p_continue(p):
    '''continue : CONTINUE SEMICOLON''' 
#######################################################################
# return
def p_return(p):
    '''return : RETURN exp SEMICOLON
              | RETURN SEMICOLON'''
#######################################################################
# block
def p_block(p):
    '''block : LBRACE init RBRACE'''
# def p_block2(p):
#     '''block : LBRACE RBRACE'''

#######################################################################
# assignation const
def p_assignation_const(p):
    '''assignation_const : CONST ID COLON type EQUAL exp '''
def p_assignation_const2(p):
    '''assignation_const : CONST ID EQUAL exp '''
#######################################################################
# assignation array
# def p_declaration_array(p):
#     '''declaration_array : declaration_type ID COLON type LBRACKET RBRACKET EQUAL defination_array SEMICOLON'''
# def p_declaration_type(p):
#     '''declaration_type : VAR
#                         | CONST'''
# def p_defination_array(p):
#     '''defination_array : LBRACKET exp_list RBRACKET
#                         | LBRACKET RBRACKET 
#                         | exp'''
# def p_exp_list(p):
#     '''exp_list : exp_list COMMA exp
#                 | exp'''
#######################################################################
# Interface
def p_interface(p):
    '''interface : INTERFACE ID LBRACE interface_body RBRACE'''
def p_interface_body(p):
    '''interface_body : interface_body SEMICOLON ID COLON type
                      | ID COLON type'''
#######################################################################
# assignation
    
# declaration with type and value
def p_assignation(p):
    '''assignation : VAR ID COLON type EQUAL exp '''
# declaration with value
def p_assignation2(p):
    '''assignation : VAR ID EQUAL exp '''
# declaration with type and without value
def p_assignation3(p):
    '''assignation : VAR ID COLON type ''' 
def p_assignation4(p):
    '''assignation : ID EQUAL exp 
                   | ID PLUS_EQUAL exp 
                   | ID MINUS_EQUAL exp '''

#######################################################################
# types
def p_type(p):
    '''type : NUMBER
            | FLOAT
            | STRING
            | CHAR
            | BOOL'''
    
#######################################################################
# expressions

def p_exp_plus(p):
    '''exp : exp PLUS exp
            | exp MINUS exp
            | exp TIMES exp
            | exp DIVIDE exp
            | exp MOD exp'''
def p_exp_unary(p):
    '''exp : MINUS exp %prec UMINUS
            | NOT exp %prec UNOT'''
    
def p_exp_comparation(p):
    '''exp : exp COMPARASION exp
            | exp DIFFERENT exp
    '''
def p_exp_relation(p):
    '''exp : exp GREATER exp
            | exp LESS exp
            | exp GREATER_EQUAL exp
            | exp LESS_EQUAL exp
    '''
def p_exp_logic(p):
    '''exp : exp AND exp
            | exp OR exp
    '''
def p_exp_literals(p):
    '''exp : NUMBER_LEX
            | FLOAT_LEX
            | STRING_LEX
            | CHAR_LEX
            | TRUE
            | FALSE
            | ID'''
def p_exp_group(p):
    '''exp : LPAREN exp RPAREN'''
def p_exp_ternary(p):
    '''exp : exp QUESTION exp COLON exp'''
def p_access_attribute(p):
    '''exp : ID DOT ID'''
#######################################################################
# empty
def p_empty(p):
    '''empty :'''
    pass
#######################################################################
# error
def p_error(p):
    if not p:
        print("The file is empty")
        return
    print("Syntax error at line " + str(p.lineno) + " token " + str(p.value))
    while True:
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'SEMICOLON' :
            break
    parser.restart()

parser = yacc.yacc()