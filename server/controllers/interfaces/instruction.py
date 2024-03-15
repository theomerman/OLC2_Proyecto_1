from abc import ABC, abstractmethod


class Instruction(ABC):
    @abstractmethod
    def run(self, context):
        pass
