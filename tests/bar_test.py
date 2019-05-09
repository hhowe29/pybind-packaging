import unittest
from foo.bar import Bar


class BarTest(unittest.TestCase):
    def test_bar(self):
        bar = Bar()
        self.assertEqual(bar.x, 29)


if __name__ == '__main__':
    unittest.main()
