import ply.yacc as yacc
from controllers.compiler.lexer import tokens
from controllers.expressions.operation import Operation
from controllers.instructions.declaration import Declaration
from controllers.expressions.access import Access
from controllers.instructions.print import Print
from controllers.instructions.assignment import Assignment
# from controllers.environment.environment import Environment
# from controllers.environment.ast import Ast
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'COMPARASION', 'DIFFERENT'),
    ('left', 'GREATER', 'LESS', 'GREATER_EQUAL', 'LESS_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'DIVIDE', 'MOD', 'TIMES'),
    ('right', 'UNOT', 'UMINUS'),

)


def p_start(p):
    '''start : init'''
    p[0] = p[1]


def p_init(p):
    '''init : init instruction
            | instruction'''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_instruction(p):
    '''instruction  : declaration SEMICOLON
                    | assignment_const SEMICOLON
                    | assignment
                    | interface
                    | if
                    | while
                    | for
                    | foreach
                    | break
                    | continue
                    | return
                    | print
    '''
    p[0] = p[1]
#######################################################################
# if


def p_if(p):
    '''if : IF LPAREN exp RPAREN block
          | IF LPAREN exp RPAREN block ELSE block
          | IF LPAREN exp RPAREN block ELSE if'''


def p_if_error(p):
    '''if : IF error '''
    print(f"Error en el else in line {p[1].lineno}, column: {p[1].lexpos}")
    pass
#######################################################################
# while


def p_while(p):
    '''while : WHILE LPAREN exp RPAREN block'''
#######################################################################
# for


def p_for(p):
    '''for : FOR LPAREN declaration SEMICOLON exp SEMICOLON declaration RPAREN block'''
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
# assignment const


def p_assignment_const(p):
    '''assignment_const : CONST ID COLON type EQUAL exp '''


def p_assignment_const2(p):
    '''assignment_const : CONST ID EQUAL exp '''
#######################################################################
# assignment array
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


def p_instruction_console(p):
    '''
    print : CONSOLE DOT LOG LPAREN exp_list RPAREN SEMICOLON
    '''
    p[0] = Print(p[5], p.lineno(5), p.lexpos(5))
#######################################################################
# Interface


def p_interface(p):
    '''interface : INTERFACE ID LBRACE interface_body RBRACE'''


def p_interface_body(p):
    '''interface_body : interface_body SEMICOLON ID COLON type
                      | ID COLON type'''
#######################################################################
# assignment

# declaration with type and value


def p_declaration(p):
    '''declaration : VAR ID COLON type EQUAL exp '''
    p[0] = Declaration(p[2], p[6], p[4], p.lineno(2), p.lexpos(2))
# declaration with value


def p_declaration2(p):
    '''declaration : VAR ID EQUAL exp '''
    p[0] = Declaration(p[2], p[4], None, p.lineno(2), p.lexpos(2))
# declaration with type and without value


def p_declaration3(p):
    '''declaration : VAR ID COLON type '''
    p[0] = Declaration(p[2], None, p[4], p.lineno(2), p.lexpos(2))


def p_declaration5(p):
    '''declaration : VAR error SEMICOLON
    '''
    print(f"Error de asignacion line: {p[2].lineno}, column: {p[2].lexpos} ")
#######################################################################
# assignment


def p_declaration4(p):
    '''assignment : ID EQUAL exp SEMICOLON
                | ID PLUS_EQUAL exp SEMICOLON
                | ID MINUS_EQUAL exp SEMICOLON '''
    p[0] = Assignment(p[1], p[2], p[3], p.lineno(1), p.lexpos(1))

#######################################################################
# types


def p_type(p):
    '''type : TYPES '''
    p[0] = p[1]
# def p_type(p):
#     '''type : NUMBER
#             | FLOAT
#             | STRING
#             | CHAR
#             | BOOL'''
#     p[0] = p[1]

#######################################################################
# expressions


def p_exp_list(p):
    '''exp_list : exp_list COMMA exp
                | exp'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_exp_plus(p):
    '''exp : exp PLUS exp
            | exp MINUS exp
            | exp TIMES exp
            | exp DIVIDE exp
            | exp MOD exp'''

    p[0] = Operation(p[1], p[2], p[3], p.lexpos(1), p.lineno(1))


def p_exp_unary(p):
    '''exp : MINUS exp %prec UMINUS
            | NOT exp %prec UNOT'''
    if p[1] == '-':
        p[0] = Operation(None, '--', p[2], p.lexpos(1), p.lineno(1))
    if p[1] == '!':
        p[0] = Operation(None, '!', p[2], p.lexpos(1), p.lineno(1))


def p_exp_comparation(p):
    '''exp : exp COMPARASION exp
            | exp DIFFERENT exp
            | exp GREATER exp
            | exp LESS exp
            | exp GREATER_EQUAL exp
            | exp LESS_EQUAL exp
            | exp AND exp
            | exp OR exp
    '''
    p[0] = Operation(p[1], p[2], p[3], p.lexpos(1), p.lineno(1))


def p_exp_literals(p):
    '''exp : NUMBER_LEX
            | FLOAT_LEX
            | STRING_LEX
            | CHAR_LEX
            | BOOLEAN
            | list_array
    '''
    p[0] = p[1]


def p_list_array(p):
    '''list_array : list_array LBRACKET exp RBRACKET
                | list_array DOT ID
                | ID
    '''
    if len(p) == 5:
        print('lista arrays')
    elif len(p) == 4:
        print('lista arrays2')
    else:
        p[0] = Access(p[1], p.lineno(1), p.lexpos(1))


def p_exp_group(p):
    '''exp : LPAREN exp RPAREN'''
    p[0] = p[2]


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
# def p_error(p):
#     if not p:
#         print("The file is empty")
#         return
#     print("Syntax error at line " + str(p.lineno) + " token " + str(p.value))
#     while True:
#         tok = parser.token()             # Get the next token
#         if not tok or tok.type == 'SEMICOLON' :
#             break
#     parser.restart()


# parser = yacc.yacc()
class Parser:
    def parse(self, data):
        parser = yacc.yacc()
        result = parser.parse(data)
        return result
