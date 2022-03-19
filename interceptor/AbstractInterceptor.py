from abc import ABC, abstractmethod

from interceptor.ContextObject import ContextObject


class AbstractInterceptor(ABC):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def execute(self, context: ContextObject):
        pass
