from controllers.interfaces.instruction import Instruction
from controllers.environment.types import ExpressionType
from controllers.environment.ast import Ast
from controllers.interfaces.expression import Expression
from controllers.environment.error import Error
from controllers.environment.symbol import Symbol
from controllers.environment.environment import Environment


class Declaration(Instruction):
    def __init__(self, id, exp: Expression, type: ExpressionType, line, column) -> None:
        self.id = id
        self.exp = exp
        self.type = type
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):

        if self.exp is None:
            set_variable_no_exp(ast, env, self.id, self.type,
                                self.line, self.column)
            # print("declaracion sin expression")
            return
        if self.type is None:
            set_variable_no_type(
                ast, env, self.id, self.exp, self.line, self.column)
            # print("declaracion sin tipo")
            return
        else:
            set_variable(ast, env, self.id, self.exp,
                         self.type, self.line, self.column)
            # print("declaracion con tipo y expresion")


def set_variable_no_exp(ast: Ast, env: Environment, id: str, type: ExpressionType, line, column):
    if id in env.table:
        ast.add_error(Error(
            f"La variable \"{id}\" ya existe",
            env.id,
            "Semantico",
            line,
            column
        )
        )
        print(f"La variable \"{id}\" ya existe")
        return
    if type is ExpressionType.NUMBER:
        env.table[id] = Symbol(line, column, 0, type)
    elif type is ExpressionType.STRING:
        env.table[id] = Symbol(line, column, "", type)
    elif type is ExpressionType.BOOLEAN:
        env.table[id] = Symbol(line, column, False, type)
    elif type is ExpressionType.CHAR:
        env.table[id] = Symbol(line, column, "", type)
    elif type is ExpressionType.FLOAT:
        env.table[id] = Symbol(line, column, 0.0, type)


def set_variable_no_type(ast: Ast, env: Environment, id: str, exp: Expression, line, column):
    if id in env.table:
        ast.add_error(Error(
            f"La variable \"{id}\" ya existe",
            env.id,
            "Semantico",
            line,
            column
        )
        )
        print(f"La variable \"{id}\" ya existe")
        return
    env.table[id] = exp.run(ast, env)


def set_variable(ast: Ast, env: Environment, id: str, exp: Expression, type: ExpressionType, line, column):
    if id in env.table:
        ast.add_error(Error(
            f"La variable \"{id}\" ya existe",
            env.id,
            "Semantico",
            line,
            column
        )
        )
        print(f"La variable \"{id}\" ya existe")
        return
    if exp.type != type:
        ast.add_error(Error(
            f"No se puede asignar un tipo \"{exp.run(ast, env).type.name}\" a un \"{type.name}\"",
            env.id,
            "Semantico",
            line,
            column
        )
        )
        print(
            f"No se puede asignar un tipo \"{exp.run(ast, env).type.name}\" a un \"{type.name}\"")
        return
    env.table[id] = exp.run(ast, env)
    # print(f"Se creo la variable {id} con el valor {env.table[id].value}")
    return
