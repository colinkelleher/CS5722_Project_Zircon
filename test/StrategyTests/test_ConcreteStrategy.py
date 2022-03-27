from unittest import TestCase
from strategy.ConcreteStrategy import ConcreteStrategy



class TestConcreteStrategy(TestCase):
    def test_complete_task(self):
        cs = ConcreteStrategy()
        test = cs.completeTask([12,13,14,15])
        self.assertEqual(test, [60,65,70,75])
