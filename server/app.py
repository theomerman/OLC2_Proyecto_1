import controllers.compiler.parser as parser

parser.parser.parse(
    '''3 "Hola";
    4 "Mundo";
    3.5 "Hola";
'''
)