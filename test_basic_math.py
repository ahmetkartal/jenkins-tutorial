import unittest


class BasicTest(unittest.TestCase):
    def setUp(self) -> None:
        self.x = 5
        self.y = 10

    def test__add_two_value(self):
        self.assertEqual(self.x + self.y, 15)


if __name__ == "__main__":
    unittest.main()
