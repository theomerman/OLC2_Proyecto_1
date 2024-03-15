from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast


class Print(Instruction):
    def __init__(self, exps: list, line, column):
        self.exps = exps
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        console = ""
        for exp in self.exps:
            value = exp.run(ast, env)
            console += str(value.value) + " "
        ast.set_console(console)
