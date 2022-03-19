from interceptor.AbstractInterceptor import AbstractInterceptor
from interceptor.ContextObject import ContextObject


class ConcreteInterceptor2(AbstractInterceptor):

    def execute(self, context: ContextObject):
        print("some other logging : \n"
              + "\n" + "interceptor-name : " + self.name
              + "\n" + "id : " + str(self.id)
              + "\n" + "name : " + context.get_name()
              + "\n" + "state : " + context.get_state()
              + "\n" + "random-parameter : " + context.get_random_parameter())
