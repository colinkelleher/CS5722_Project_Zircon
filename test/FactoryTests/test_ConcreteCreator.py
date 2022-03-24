from unittest import TestCase

from factory.FactoryMethod import MapGeneratorSimple, client_code

class TestConcreteCreator(TestCase):
    def test_ConcreteCreator(self):
        mgs = MapGeneratorSimple()
        self.assertTrue(client_code(mgs) == print("Simple Map is used."))
