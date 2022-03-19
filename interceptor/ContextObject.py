class ContextObject:

    def __init__(self, framework):
        self.framework = framework

    def get_state(self):
        return self.framework.state

    def get_name(self):
        return self.framework.name

    def get_random_parameter(self):
        return self.framework.random_parameter
