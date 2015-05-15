import unittest

from Task_01.task_01 import *

class Task01_tests(unittest.TestCase):
    def test_nimi_exists(self):
        self.assertTrue('nimi' in globals(), 'Lisasithan varmasti muuttujan nimi?')
        pass

    def test_nimi_notEmpty(self):
        nimi_empty = 'nimi' in globals()
        self.assertTrue(nimi_empty and nimi, 'nimi ei saa olla tyhja')
        pass

    def test_lempi_elokuva_not_None(self):
        self.assertTrue(not lempielokuva is None, 'lempielokuva ei saa olla maarittelematon (null)')
        pass

    def test_lempi_elokuva_not_empty(self):
        self.assertTrue(lempielokuva, 'lempielokuva ei saa olla tyhja')
        pass

    def test_elokuva_returns_right(self):
        self.assertEqual('Kaapon lempielokuva on \"Nallen puisto\"', lempi_elokuva('Kaapo', 'Nallen puisto'))
        pass

    def test_sanan_pituus_correct(self):
        self.assertEqual(4, '1234')
        pass

    def test_eka_vika_works(self):
        self.assertEqual('Ko', eka_vika('Kaapo'))
        pass

    def test_kaantaen(self):
        self.assertEqual('opaaK', kaantaen('Kaapo'))

    def test_onko_palindromi(self):
        self.assertEqual(True, onko_palindromi("AABBBAA"))

    def test_listaan(self):
        self.assertEqual([1, 2, 3, 4], listaan(1, 2, 3, 4))

    def test_indeksiin_asti(self):
        self.assertEqual([1, 2, 3], indeksiin_asti([1, 2, 3, 4, 5, 6], 3))

    def test_vaihda_luku(self):
        self.assertEqual([1, 2, 3], vaihda_luku([1, 2, 4], 3, 3))

    def test_yhdista_taulut(self):
        self.assertEqual([1, 2, 3, 4], yhdista_taulut([1, 2], [3, 4]))

    def test_capslockkaa(self):
        k = [['a'], ['b'], ['c']]
        self.assertEqual([['A'], ['B'], ['C']], capslockkaa(k))

    def test_fibonacci(self):
        self.assertEqual(55, fibonacci(10))

    def test_eka_rekursio(self):
        self.assertEqual('', eka_rekursio('Kaaleppi soi omenan.'))

if __name__ == '__main__':
    unittest.main()
