from __future__ import annotations

class Context():
    def __init__(self, strategy:Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self)-> Strategy:
        return self._strategy

    def setstrategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def businessLogic(self)-> str:
        x = self.strategy.selection()
        return x
