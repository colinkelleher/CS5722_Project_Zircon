from typing import List

from interceptor.AbstractInterceptor import AbstractInterceptor


class Dispatcher:

    def __init__(self, interceptors: List[AbstractInterceptor]):
        self.context = None
        self.head_interceptor: AbstractInterceptor = interceptors[0]

        if len(interceptors) > 1:
            current_interceptor = self.head_interceptor
            for interceptor in interceptors[1:]:
                current_interceptor.next_interceptor = interceptor
                current_interceptor = interceptor

    def attach_interceptor(self, new_interceptor: AbstractInterceptor):
        interceptor = self.head_interceptor
        while interceptor.next_interceptor is not None:
            interceptor = interceptor.next_interceptor
        interceptor.next_interceptor = new_interceptor

    def detach_interceptor(self, interceptor_to_delete: AbstractInterceptor) -> None:

        if self.head_interceptor is not None and self.head_interceptor.id == interceptor_to_delete.id:
            self.head_interceptor = self.head_interceptor.next_interceptor

        interceptor = self.head_interceptor
        previvous_interceptor = None
        while interceptor is not None:
            if interceptor.id == interceptor_to_delete.id:
                break
            previvous_interceptor = interceptor
            interceptor = interceptor.next_interceptor
        previvous_interceptor.next_interceptor = interceptor.next_interceptor
        interceptor = None

    def get_total_interceptor_count(self) -> int:
        count = 0
        interceptor = self.head_interceptor
        while interceptor is not None:
            count += 1
            interceptor = interceptor.next_interceptor
        return count

    def execute(self, request_type: str):
        self.head_interceptor.execute(self.context, request_type)
