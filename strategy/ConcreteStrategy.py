from __future__ import annotations
from typing import List

class ConcreteStrategy():
    def completeTask(self, data:List) -> List:
        data = [i * 5 for i in data]
        return data
