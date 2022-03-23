from unittest import TestCase

from engine.Engine import Engine


class TestEngine(TestCase):
    def test_singleton_pattern(self):
        engine1 = Engine()
        engine2 = Engine()
        self.assertEqual(id(engine1), id(engine2), 'Singleton Failed')
