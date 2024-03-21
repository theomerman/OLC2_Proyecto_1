# import controllers.compiler.parser as parser
from controllers.compiler.parser import Parser
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast

env = Environment(None, "global")
ast = Ast()

parser = Parser()

data = '''

'''

instuctions = parser.parse(data)
for intruction in instuctions:
    intruction.run(ast, env)

for error in ast.get_errors():
    print(error.description)

print(ast.get_console(), end='')
