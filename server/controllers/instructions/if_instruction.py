from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType


class If(Instruction):
    def __init__(self, ctx: list, line, column):
        self.ctx = ctx
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        for arr in self.ctx:
            if arr[0].run(ast, env).type != ExpressionType.BOOLEAN:
                ast.add_error(Error(
                    "La condición del if debe ser de tipo booleano",
                    env.id,
                    "Semántico",
                    self.line,
                    self.column
                ))
                return
            if arr[0].run(ast, env).value == True:
                for inst in arr[1]:
                    inst.run(ast, env)
                break
