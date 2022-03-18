from unittest import TestCase
from system.System import System


class TestSystem(TestCase):
    def test_System_Creation_With_Id(self):
        system = System(1)
        self.assertEqual(system.system_id, 1, 'Id is not equal to supposed value')
