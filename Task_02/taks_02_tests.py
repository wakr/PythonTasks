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

    def test_alusta_loppuun_listaan(self):
        self.assertEqual([1, 2, 3], alusta_loppuun_listaan(1, 3))
        self.assertEqual([99, 100], alusta_loppuun_listaan(99, 100))
        self.assertEqual([-1, -2, -3], alusta_loppuun_listaan(-1, -3))

    def test_erittele_parilliset(self):
        self.assertEqual([2, 4, 6], erittele_pariliset(range(1, 7)))
        self.assertEqual(list(range(2, 100, 2)), erittele_pariliset(list(range(1, 100))))

    def test_henkilotieto_tulostin(self):
        self.assertEqual("Pultun syntymavuosi on 1992 ja han tykkaa sukluusta", henkilotieto_tulostin(**henkilo))

    def test_paranneltu_henkilo_tulostin(self):
        self.assertEqual("Pultun syntymavuosi on 1992 ja han tykkaa sukluusta", paranneltu_henkilo_tulostin(henkilo))

    def test_tulostus_natiksi(self):
        self.assertTrue(tulostus_natiksi(henkilo).startswith("{\n"),
                        msg="Aloittavan hakasulun jalkeen pitaisi olla rivinvaihto")
        self.assertTrue(tulostus_natiksi(henkilo).endswith("\n}"),
                        msg="Ennen viimeista hakasulkua pitaisi olla rivinvaihto")
        self.assertTrue(tulostus_natiksi(henkilo).splitlines().__len__() == len(henkilo) + 2,
                        msg="Rivien lkm on vaara.")
        # 2 is the generated { and }

if __name__ == '__main__':
    unittest.main()
