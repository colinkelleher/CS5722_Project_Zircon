from unittest import TestCase
from factory.RoomObject import RectangularRoom


class TestRectangularRoom(TestCase):
    def test_center(self):
        rr = RectangularRoom(2,4,10,10)
        rr_c = rr.center
        self.assertEqual(rr_c[0], 7 )
        self.assertEqual(rr_c[1], 9 )

    def test_inner(self):
        rr = RectangularRoom(2,4,10,10)
        innare = rr.inner
        self.assertEqual(innare,(slice(3, 12, None), slice(5, 14, None)))

    def test_intersects(self):
        rr = RectangularRoom(2,4,10,10)
        intr = rr.intersects(RectangularRoom(3,10,12,10))
        self.assertTrue(intr)
