from interceptor.AbstractInterceptor import AbstractInterceptor
from interceptor.ContextObject import ContextObject


class InputLoggingInterceptor(AbstractInterceptor):

    def execute(self, context: ContextObject, request_type: str) -> None:

        if request_type == "Input":

            print("some logging : \n"
                  + "\n" + "interceptor-name : " + self.name
                  + "\n" + "id : " + str(self.id)
                  + "\n" + "name : " + context.get_name()
                  + "\n" + "state : " + context.get_state()
                  + "\n" + "random-parameter : " + context.get_random_parameter()
                  + "\n")
        else:
            super().execute(context, request_type)
