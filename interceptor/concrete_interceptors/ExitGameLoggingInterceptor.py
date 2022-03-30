from interceptor.AbstractInterceptor import AbstractInterceptor
from interceptor.ContextObject import ContextObject


class ExitGameLoggingInterceptor(AbstractInterceptor):

    def execute(self, context: ContextObject, request_type: str):
        if request_type == "Exit":

            print("some other logging : \n"
                  + "\n" + "interceptor-name : " + self.name
                  + "\n" + "id : " + str(self.id)
                  + "\n" + "name : " + context.get_name()
                  + "\n" + "state : " + context.get_state()
                  + "\n" + "random-parameter : " + context.get_random_parameter())
        else:
            super().execute(context, request_type)
