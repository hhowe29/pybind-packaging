import unittest
import foo


class FooTest(unittest.TestCase):
    def test_bar(self):
        f = foo.Foo()
        self.assertEqual(f.x, 42)


if __name__ == '__main__':
    unittest.main()
