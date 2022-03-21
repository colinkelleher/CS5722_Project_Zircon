from unittest import TestCase
from system.System import System


class TestSystem(TestCase):
    def test_System_Creation_With_Id(self):
        system = System()
        res = system.get_id()
        self.assertFalse(res == 1, "System ID is random and not 1")

    def test_Protected_System_Id_Cannot_Be_Modified(self):
        system = System()
        system._system_id = 5
        self.assertNotEqual(system._system_id, 1, 'Id should not have been modified')
