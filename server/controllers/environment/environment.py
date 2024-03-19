from controllers.environment.symbol import Symbol
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType


class Environment:
    def __init__(self, previus, id: str):
        self.previus = previus
        self.id = id
        self.table = {}
        self.interfaces = {}
        self.functions = {}

    def save_variable(self, ast: Ast, id: str, symbol: Symbol, line, column):
        if id in self.table:
            ast.add_error(Error(
                f"La variable \"{id}\" ya existe",
                self.id,
                "Semantico",
                line,
                column
            )
            )
            return
        self.table[id] = symbol

    def get_variable(self, ast: Ast, id: str):
        if id in self.table:
            return self.table[id]
        if self.previus is not None:
            return self.previus.get_variable(id)
        ast.add_error(Error(
            f"La variable \"{id}\" no existe",
            self.id,
            "Semantico",
            0,
            0
        )
        )
        return Symbol(0, 0, ExpressionType.NULL.name, ExpressionType.NULL)

    def update_variable(self, ast: Ast, id: str, operator: str, symbol: Symbol, line, column):
        if id in self.table:

            if self.table[id].constant:
                ast.add_error(Error(
                    f"La variable \"{id}\" es constante y no se puede modificar",
                    self.id,
                    "Semantico",
                    line,
                    column
                )
                )
                return

            if self.table[id].type != symbol.type:
                ast.add_error(Error(
                    f"La variable \"{id}\" no es del mismo tipo",
                    self.id,
                    "Semantico",
                    line,
                    column
                )
                )
                return
            if operator == "=":
                self.table[id] = symbol
                return
            elif operator == "+=":
                if self.table[id].type not in [ExpressionType.NUMBER, ExpressionType.STRING, ExpressionType.FLOAT]:
                    ast.add_error(Error(
                        f"No se puede incrementar una variable de tipo {self.table[id].type}",
                        self.id,
                        "Semantico",
                        line,
                        column
                    )
                    )
                    return
                if self.table[id].type == symbol.type:
                    self.table[id].value += symbol.value
                    return
                return
            elif operator == "-=":
                if self.table[id].type not in [ExpressionType.NUMBER, ExpressionType.FLOAT]:
                    ast.add_error(Error(
                        f"No se puede decrementar una variable de tipo {self.table[id].type}",
                        self.id,
                        "Semantico",
                        line,
                        column
                    )
                    )
                    return
                if self.table[id].type == symbol.type:
                    self.table[id].value -= symbol.value
                    return
                return
            return
        if self.previus is not None:
            self.previus.update_variable(id, symbol)
            return
        ast.add_error(Error(
            f"La variable \"{id}\" no existe",
            self.id,
            "Semantico",
            line,
            column
        )
        )
