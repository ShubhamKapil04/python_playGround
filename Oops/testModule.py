import unittest

from myModule import square, doubler


class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEquals(square(3), 9)
        self.assertEquals(square(6), 36)
        self.assertEquals(square(-3.0), 9.0)

    def test_doubler(self):
        self.assertEquals(doubler(2), 4)
        self.assertEquals(doubler(-5), 10)


unittest.main()
