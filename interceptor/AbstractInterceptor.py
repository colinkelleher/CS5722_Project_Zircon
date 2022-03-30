from __future__ import annotations

from abc import ABC, abstractmethod

from interceptor.ContextObject import ContextObject


class AbstractInterceptor(ABC):

    def __init__(self, id, name):
        self.next_interceptor: AbstractInterceptor = None
        self.id = id
        self.name = name

    @abstractmethod
    def execute(self, context: ContextObject, request_type: str) -> None:   # chain of responsability call
        if self.next_interceptor:
            self.next_interceptor.execute(context, request_type)
        else:
            print("\nNo interceptor can handle the request : " + request_type)

    def set_next(self, interceptor: AbstractInterceptor) -> AbstractInterceptor:
        self.next_interceptor = interceptor
        return interceptor


