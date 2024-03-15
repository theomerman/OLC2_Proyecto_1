# import controllers.compiler.parser as parser
from controllers.compiler.parser import Parser
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast

env = Environment(None, "global")
ast = Ast()

parser = Parser()

data = '''
var x = "hola ";
x += "mundo";
var y = 5.3;
y -= 2.3;
console.log(y);
'''
instuctions = parser.parse(data)
for intruction in instuctions:
    intruction.run(ast, env)
print(ast.get_console(), end='')
