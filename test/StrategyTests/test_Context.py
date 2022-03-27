from unittest import TestCase
from strategy.Context import Context
from strategy.ConcreteStrategy import ConcreteStrategy


class TestContext(TestCase):
    def test_business_logic(self):
        context = Context(ConcreteStrategy())
        self.assertEqual(context.businessLogic(),[5,10,15,20,25])

