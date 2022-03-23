from unittest import TestCase

from entity.Enemy import Enemy


class TestEnemy(TestCase):
    def test_init_with_empty_components(self):
        enemy = Enemy()
        self.assertEqual(len(enemy.components), 0, "Length of Components list was not empty")
