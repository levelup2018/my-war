import unittest
import war

class TestWvsW(unittest.TestCase):
    def setUp(self):
        self.unit1 = war.Warrior()
        self.unit2 = war.Warrior()

    def test_is_alive(self):
        self.assertTrue(self.unit1.is_alive())
        self.assertTrue(self.unit2.is_alive())

    def test_one_kick(self):
        self.assertEqual(self.unit1.health, 20)
        self.assertEqual(self.unit2.health, 20)

        self.unit1.kick(self.unit2)

        self.assertEqual(self.unit1.health, 20)
        self.assertEqual(self.unit2.health, 10)


if __name__ == '__main__':
    unittest.main()