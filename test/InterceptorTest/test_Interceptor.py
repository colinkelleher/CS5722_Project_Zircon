from unittest import TestCase

from interceptor.ContextObject import ContextObject
from interceptor.Dispatcher import Dispatcher
from interceptor.concrete_interceptors.ExitGameLoggingInterceptor import ExitGameLoggingInterceptor
from interceptor.Framework import Framework
from interceptor.concrete_interceptors.InputLoggingInterceptor import InputLoggingInterceptor


def interception_method(dispatcher: Dispatcher, context: ContextObject, request_type: str):
    dispatcher.context = context
    dispatcher.execute(request_type)


class TestInterceptor(TestCase):
    def test_interceptor(self):
        ##Framework Object is simulating the framework behaviour
        framework = Framework("framework1", "stable", "random-parameter1")
        context = ContextObject(framework)

        concrete_interceptor_1 = InputLoggingInterceptor(1, "interceptor1")
        concrete_interceptor_2 = InputLoggingInterceptor(2, "interceptor2")
        concrete_interceptor_3 = ExitGameLoggingInterceptor(3, "interceptor3")

        interceptors = [concrete_interceptor_1, concrete_interceptor_2]
        dispatcher = Dispatcher(interceptors)

        dispatcher.attach_interceptor(concrete_interceptor_3)
        self.assertEqual(3, dispatcher.get_total_interceptor_count())

        dispatcher.detach_interceptor(concrete_interceptor_2)
        self.assertEqual(2, dispatcher.get_total_interceptor_count())
        self.assertEqual("interceptor1", dispatcher.head_interceptor.name)
        self.assertEqual("interceptor3", dispatcher.head_interceptor.next_interceptor.name)

        ##Interception Point is triggered
        interception_method(dispatcher, context, "Input")
        interception_method(dispatcher, context, "Exit")
        interception_method(dispatcher, context, "random_interception_point")
