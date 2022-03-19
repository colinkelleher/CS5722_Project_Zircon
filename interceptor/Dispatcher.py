class Dispatcher:

    def __init__(self, interceptors):
        self.context = None
        self.interceptors = []
        for interceptor in interceptors:
            self.interceptors.append(interceptor)

    def attach_interceptor(self, new_interceptor):
        self.interceptors.append(new_interceptor)

    def detach_interceptor(self, interceptor_to_delete):
        for index, interceptor in enumerate(self.interceptors):
            if interceptor.id == interceptor_to_delete.id:
                del self.interceptors[index]
                break

    def execute(self):
        for interceptor in self.interceptors:
            interceptor.execute(self.context)
