import unittest

import Task_02.task_02 as Task02
from Task_02.task_02 import *


def moc_input(s):
    return 11


class MyTestCase(unittest.TestCase):
    def setUp(self):
        Task02.input = moc_input

    def test_kerro_arvo(self):
        self.assertEqual("jeejee", kerro_arvo())

    def test_fizz_buzz(self):
        self.assertEqual("Fizz", fizz_buzz(6))
        self.assertEqual("Buzz", fizz_buzz(50))
        self.assertEqual("FizzBuzz", fizz_buzz(30))

    def test_suuret_alkuun(self):
        self.assertEqual([10, 8, 6, 4, 2, 1, 3, 5, 7, 9], suuret_alkuun())

    def test_pisin_sanat(self):
        self.assertEqual("Kaapon kesavene", pisin_sana(["Auto", "Makkaru", "Pekan kesavene", "Kaapon kesavene"]))
        self.assertEqual("Makkaruuuuuuuuuu",
                         pisin_sana(["Auto", "Makkaruuuuuuuuuu", "Pekan kesavene", "Kaapon kesavene"]))

    def test_pisimman_indeksi(self):
        self.assertEqual(("AA", 0), pisimman_indeksi(["AA", "B", "C"]))
        self.assertEqual(("AA", 2), pisimman_indeksi(["AA", "BBBB", "CCCCC"]))





if __name__ == '__main__':
    unittest.main()
