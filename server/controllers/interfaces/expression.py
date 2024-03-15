from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def run(self, context): pass
