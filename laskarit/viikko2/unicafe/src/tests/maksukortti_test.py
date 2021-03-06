import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_lataaminen_oikein(self):
        self.maksukortti.lataa_rahaa(40)
        self.assertEqual(str(self.maksukortti), "saldo: 0.5")

    def test_ottaminen_kun_on_rahaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_ottaminen_kun_ei_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ottaminen_tosi_kun_on_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_ottaminen_epatosi_kun_on_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), False)
