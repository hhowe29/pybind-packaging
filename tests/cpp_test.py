import unittest
from foo import add


class BazTest(unittest.TestCase):
    def test_addr(self):
        observed = add(29, 41)
        self.assertEqual(observed, 70)


if __name__ == '__main__':
    unittest.main()
