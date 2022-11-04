import unittest


class BasicTest(unittest.TestCase):
    def setUp(self) -> None:
        self.x = 5
        self.y = 10

    def test__add_two_value(self):
        self.assertEqual(self.x + self.y, 15)

    def test__sub_two_value(self):
        self.assertEqual(self.y - self.x, 5)

    def test__div_two_value(self):
        self.assertEqual(self.y / self.x, 2)


if __name__ == "__main__":
    print("sixth buildtest")
    unittest.main()
