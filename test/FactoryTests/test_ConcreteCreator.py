from unittest import TestCase

from factory.FactoryMethod import MapGeneratorSimple

class TestConcreteCreator(TestCase):
    def test_ConcreteCreator(self):
        mgs = MapGeneratorSimple()
        result: str = mgs.create_map()
        self.assertTrue(result == "Simple Map is used.")
