from unittest import TestCase

from interceptor.Dispatcher import Dispatcher
from interceptor.ConcreteInterceptor1 import ConcreteInterceptor1
from interceptor.ConcreteInterceptor2 import ConcreteInterceptor2
from interceptor.ContextObject import ContextObject
from interceptor.Framework import Framework


def interception_method(dispatcher: Dispatcher, context: ContextObject):
    dispatcher.context = context
    dispatcher.execute()


class TestInterceptor(TestCase):
    def test_interceptor(self):
        ##Framework Object is simulating the framework behaviour
        framework = Framework("framework1", "stable", "random-parameter1")
        context = ContextObject(framework)

        concrete_interceptor_1 = ConcreteInterceptor1(1, "interceptor1")
        concrete_interceptor_2 = ConcreteInterceptor1(2, "interceptor2")
        concrete_interceptor_3 = ConcreteInterceptor1(3, "interceptor3")
        interceptors = [concrete_interceptor_1, concrete_interceptor_2]
        dispatcher = Dispatcher(interceptors)

        dispatcher.attach_interceptor(concrete_interceptor_3)
        self.assertEqual(3, len(dispatcher.interceptors))

        dispatcher.detach_interceptor(concrete_interceptor_2)
        self.assertEqual(2, len(dispatcher.interceptors))
        self.assertEqual("interceptor1", dispatcher.interceptors[0].name)
        self.assertEqual("interceptor3", dispatcher.interceptors[1].name)

        ##Interception Point is triggered
        interception_method(dispatcher, context)
