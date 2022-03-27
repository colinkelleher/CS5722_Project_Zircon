from __future__ import annotations

class Context():
    def __init__(self, strategy:Strategy) -> None:
        self._strategy = strategy

    @property
    def getStrategy(self)-> Strategy:
        return self._strategy

    @setStrategy.setter
    def setStrategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

