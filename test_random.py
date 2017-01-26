import unittest
import random


class TestRandom(unittest.TestCase):

    def setUp(self):
        self.seeder = random.randint(1, 99999)

    def test_seeder_1(self):
        av = self.seeder * 666
        result = av > 0
        self.assertTrue(result > 0)

    def test_seeder_2(self):
        av = self.seeder * 666
        result = av > 0
        self.assertTrue(result > 0)

    def test_seeder_3(self):
        av = self.seeder * 666
        result = av > 0
        self.assertTrue(result > 0)

    def test_seeder_4(self):
        av = self.seeder * 666
        result = av > 0
        self.assertTrue(result > 0)

    def test_seeder_5(self):
        av = self.seeder * 666
        result = av > 0
        self.assertTrue(result > 0)

    def test_seeder_6(self):
        av = self.seeder * 666
        result = av > 0
        self.assertTrue(result > 0)


if __name__ == "__main__":
    unittest.main()
