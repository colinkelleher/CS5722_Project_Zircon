'''
Strategy Interface

Context can use this interface to call algorithm defined by Concrete Strategy
'''

from abc import ABC,abstractmethod
from typing import List


class Stategy(ABC):
    @abstractmethod
    def algoirthm(self,data:List):
        pass