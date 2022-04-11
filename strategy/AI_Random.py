from __future__ import annotations
from strategy.Strategy import Strategy
import random

class AI_Random (Strategy):
    def selection(self) -> str:
        options = ["Articial Intelligence Level 1","Articial Intelligence Level 2","Articial Intelligence Level 3" ]
        print(random.choice(options))