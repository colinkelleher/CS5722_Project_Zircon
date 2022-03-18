from unittest import TestCase
from system.System import System


class TestSystem(TestCase):
    def test_System_Creation_With_Id(self):
        system = System(1)
        self.assertEqual(system._system_id, 1, 'Id is not equal to supposed value')

    def test_Protected_System_Id_Cannot_Be_Modified(self):
        system = System(1)
        system._system_id = 5
        self.assertEqual(system._system_id, 1, 'Id should not have been modified')
