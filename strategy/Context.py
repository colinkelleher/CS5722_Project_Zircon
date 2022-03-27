from __future__ import annotations

class Context():
    def __init__(self, strategy:Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self)-> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def businessLogic(self)-> List:
        # Testing random business logic here - Any task can be put here
        result = self._strategy.completeTask([1,2,3,4,5])
        return result
