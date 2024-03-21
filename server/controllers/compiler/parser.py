import ply.yacc as yacc
import numpy as np
from controllers.compiler.lexer import tokens
from controllers.expressions.operation import Operation
from controllers.instructions.declaration import Declaration
from controllers.expressions.access import Access
from controllers.expressions.ternary import Ternary
from controllers.instructions.print import Print
from controllers.instructions.assignment import Assignment
from controllers.instructions.array_declaration import ArrayDeclaration
from controllers.expressions.primitive import Primitive
from controllers.environment.types import ExpressionType
from controllers.expressions.access_array import AccessArray
from controllers.instructions.array_assignment import ArrayAssignment
from controllers.instructions.push import Push
from controllers.expressions.vector_functions import VectorFunctions
from controllers.expressions.embed_functions import EmbedFunctions
from controllers.instructions.if_instruction import If
from controllers.instructions.for_instruction import For
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
    '''start : block'''
    p[0] = p[1]


def p_init(p):
    '''block : block instruction
            | instruction'''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_instruction(p):
    '''instruction  : assignment
                    | declaration
                    | declaration_array
                    | declaration_matrix
                    | vector_functions
                    | interface
                    | if_statement
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


# def p_if(p):
#     '''if : IF LPAREN exp RPAREN block
#           | IF LPAREN exp RPAREN block ELSE block
#           | IF LPAREN exp RPAREN block ELSE if'''

def p_if_statement(p):
    '''if_statement : if'''
    p[0] = If(p[1], p.lineno(1), p.lexpos(1))


def p_if_1(p):
    '''if : IF LPAREN exp RPAREN LBRACE block RBRACE ELSE if'''
    p[0] = [[p[3], p[6]]] + p[9]


def p_if_3(p):
    '''if : IF LPAREN exp RPAREN LBRACE block RBRACE'''
    p[0] = [[p[3], p[6]]]


def p_if_2(p):
    '''if : IF LPAREN exp RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE'''
    p[0] = [[p[3], p[6]], [Primitive(
        True, ExpressionType.BOOLEAN, p.lineno(1), p.lexpos(1)), p[10]]]


#######################################################################
# while


def p_while(p):
    '''while : WHILE LPAREN exp RPAREN block'''
#######################################################################
# for


def p_for(p):
    '''for : FOR LPAREN declaration exp SEMICOLON declaration RPAREN LBRACE block RBRACE'''
    p[0] = For()

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


# def p_block(p):
#     '''block : LBRACE init RBRACE'''
# def p_block2(p):
#     '''block : LBRACE RBRACE'''

#######################################################################
# print


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
# declaration vector
def p_declaration_array(p):
    '''declaration_array : VAR ID COLON type LBRACKET RBRACKET EQUAL definition_array SEMICOLON'''
    p[0] = ArrayDeclaration(False, p[2], p[4], 1, p[8],
                            p.lineno(2), p.lexpos(2))


def p_declaration_array_error(p):
    '''declaration_array : VAR ID COLON type LBRACKET RBRACKET EQUAL error SEMICOLON'''
    print("Error en la declaracion de array ")
    p[0] = Primitive(
        ExpressionType.NULL.name, ExpressionType.NULL, p.lineno(2), p.lexpos(2))


def p_declaration_array2(p):
    '''declaration_array : CONST ID COLON type LBRACKET RBRACKET EQUAL definition_array SEMICOLON'''
    p[0] = ArrayDeclaration(True, p[2], p[4], 1, p[8],
                            p.lineno(2), p.lexpos(2))


def p_defination_array(p):
    '''definition_array : LBRACKET exp_list RBRACKET
                        | LBRACKET RBRACKET
                        | exp'''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 3:
        p[0] = []
    elif len(p) == 2:
        p[0] = p[1]


#######################################################################
# declaration matrix


def p_declaration_matrix(p):
    '''declaration_matrix : VAR ID COLON type matrix_dimension EQUAL LBRACKET values_list RBRACKET SEMICOLON'''
    p[0] = ArrayDeclaration(False, p[2], p[4], p[5],
                            p[8], p.lineno(2), p.lexpos(2))


def p_declaration_matrix2(p):
    '''declaration_matrix : CONST ID COLON type matrix_dimension EQUAL LBRACKET values_list RBRACKET SEMICOLON'''
    p[0] = ArrayDeclaration(True, p[2], p[4], p[5],
                            p[8], p.lineno(2), p.lexpos(2))


def p_matrix_dimension(p):
    '''matrix_dimension : matrix_dimension LBRACKET RBRACKET
                        | LBRACKET RBRACKET LBRACKET RBRACKET'''
    if len(p) == 4:
        p[0] = p[1] + 1
    else:
        p[0] = 2


def p_values_list(p):
    '''values_list : values_list COMMA LBRACKET arg RBRACKET
                    | LBRACKET arg RBRACKET'''
    if len(p) == 6:
        p[1].append(p[4])
        p[0] = p[1]
    else:
        p[0] = [p[2]]


def p_arg(p):
    '''arg : values_list
            | exp_list'''
    p[0] = p[1]

#######################################################################
# vector functions


def p_vector_functions(p):
    '''vector_functions : ID DOT PUSH LPAREN exp RPAREN SEMICOLON'''
    p[0] = Push(p[1], p[5], p.lineno(1), p.lexpos(1))


def p_vector_expression(p):
    '''exp : ID DOT POP LPAREN RPAREN'''
    p[0] = VectorFunctions(p[1], p[3], p[5], p.lineno(1), p.lexpos(1))


def p_vector_expression2(p):
    '''exp : ID DOT INDEXOF LPAREN exp RPAREN'''
    p[0] = VectorFunctions(p[1], p[3], p[5], p.lineno(1), p.lexpos(1))


def p_vector_expression3(p):
    '''exp : ID DOT JOIN LPAREN RPAREN'''
    p[0] = VectorFunctions(p[1], p[3], p[5], p.lineno(1), p.lexpos(1))


def p_vector_expression4(p):
    '''exp : ID DOT LENGTH'''
    p[0] = VectorFunctions(p[1], p[3], p[3], p.lineno(1), p.lexpos(1))
#######################################################################
# embed functions


def p_embed_functions(p):
    '''exp : PARSEINT LPAREN exp RPAREN'''
    p[0] = EmbedFunctions(p[1], p[3], p.lineno(1), p.lexpos(1))


def p_embed_functions2(p):
    '''exp : PARSEFLOAT LPAREN exp RPAREN'''
    p[0] = EmbedFunctions(p[1], p[3], p.lineno(1), p.lexpos(1))


def p_embed_functions3(p):
    '''exp : exp DOT TOSTRING LPAREN RPAREN'''
    p[0] = EmbedFunctions(p[3], p[1], p.lineno(1), p.lexpos(1))


def p_embed_functions3_1(p):
    '''exp : ID DOT TOSTRING LPAREN RPAREN'''
    p[0] = EmbedFunctions(p[3], p[1], p.lineno(1), p.lexpos(1))


def p_embed_functions4(p):
    '''exp : exp DOT TOLOWERCASE LPAREN RPAREN'''
    p[0] = EmbedFunctions(p[3], p[1], p.lineno(1), p.lexpos(1))


def p_embed_functions4_1(p):
    '''exp : ID DOT TOLOWERCASE LPAREN RPAREN'''
    p[0] = EmbedFunctions(p[3], p[1], p.lineno(1), p.lexpos(1))


def p_embed_functions5(p):
    '''exp : exp DOT TOUPPERCASE LPAREN RPAREN'''
    p[0] = EmbedFunctions(p[3], p[1], p.lineno(1), p.lexpos(1))


def p_embed_functions5_1(p):
    '''exp : ID DOT TOUPPERCASE LPAREN RPAREN'''
    p[0] = EmbedFunctions(p[3], p[1], p.lineno(1), p.lexpos(1))


def p_embed_functions6(p):
    '''exp : TYPEOF exp'''
    p[0] = EmbedFunctions(p[1], p[2], p.lineno(1), p.lexpos(1))
#######################################################################
# declaration const


def p_declaration_const(p):
    '''declaration : CONST ID COLON type EQUAL exp SEMICOLON'''
    p[0] = Declaration(p[2], p[6], p[4], p.lineno(2), p.lexpos(2), True)


def p_declaration_const2(p):
    '''declaration : CONST ID EQUAL exp SEMICOLON'''
    p[0] = Declaration(p[2], p[4], None, p.lineno(2), p.lexpos(2), True)

#######################################################################
# declaration

# declaration with type and value


def p_declaration(p):
    '''declaration : VAR ID COLON type EQUAL exp SEMICOLON'''
    p[0] = Declaration(p[2], p[6], p[4], p.lineno(2), p.lexpos(2))
# declaration with value


def p_declaration2(p):
    '''declaration : VAR ID EQUAL exp SEMICOLON '''
    p[0] = Declaration(p[2], p[4], None, p.lineno(2), p.lexpos(2))
# declaration with type and without value


def p_declaration3(p):
    '''declaration : VAR ID COLON type SEMICOLON'''
    p[0] = Declaration(p[2], None, p[4], p.lineno(2), p.lexpos(2))


# def p_declaration5(p):
#     '''declaration : VAR error SEMICOLON
#     '''
#     print(f"Error de asignacion line: {p[2].lineno}, column: {p[2].lexpos} ")
#######################################################################
# assignment


def p_declaration4(p):
    '''assignment : ID EQUAL exp SEMICOLON
                | ID PLUS_EQUAL exp SEMICOLON
                | ID MINUS_EQUAL exp SEMICOLON '''
    p[0] = Assignment(p[1], p[2], p[3], p.lineno(1), p.lexpos(1))


def p_declaration5(p):
    '''assignment : ID index_list EQUAL exp SEMICOLON'''
    p[0] = ArrayAssignment(p[1], p[2], p[4], p.lineno(1), p.lexpos(1))


def p_index_list(p):
    '''index_list : index_list LBRACKET exp RBRACKET
                | LBRACKET exp RBRACKET'''
    if len(p) == 5:
        p[1].append(p[3])
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = [p[2]]
#######################################################################
# types


def p_type(p):
    '''type : TYPES '''
    p[0] = p[1]

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
            | list_access
    '''
    p[0] = p[1]


def p_list_access(p):
    '''list_access : list_access LBRACKET exp RBRACKET
                | list_access DOT ID
                | ID
    '''
    if len(p) == 5:
        if isinstance(p[1], Access):
            access = AccessArray(p[1], p.lineno(1), p.lexpos(1))
            access.indexes.append(p[3])
            p[0] = access
        elif isinstance(p[1], AccessArray):
            p[1].indexes.append(p[3])
            p[0] = p[1]
        else:
            print("No se puede acceder a un valor que no sea primitivo en un array")
            p[0] = Primitive(ExpressionType.NULL.name,
                             ExpressionType.NULL, p.lineno(1), p.lexpos(1))
    elif len(p) == 4:
        print('structs access')
    else:
        p[0] = Access(p[1], p.lineno(1), p.lexpos(1))


def p_exp_group(p):
    '''exp : LPAREN exp RPAREN'''
    p[0] = p[2]


def p_exp_ternary(p):
    '''exp : exp QUESTION exp COLON exp'''
    p[0] = Ternary(p[1], p[3], p[5], p.lineno(1), p.lexpos(1))


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
