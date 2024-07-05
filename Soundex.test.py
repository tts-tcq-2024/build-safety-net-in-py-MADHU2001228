import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_generate_soundex_empty(self):
        self.assertEqual(generate_soundex(""), "")

    def test_generate_soundex_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")
        self.assertEqual(generate_soundex("1"), "1000")

    def test_generate_soundex_basic(self):
        self.assertEqual(generate_soundex("AB"), "A100")
        self.assertEqual(generate_soundex("AI"), "A000")
        self.assertEqual(generate_soundex("ART"), "A630")
        self.assertEqual(generate_soundex("ARD"), "A630")

    def test_generate_soundex_complex(self):
        self.assertEqual(generate_soundex("Flower"), "F460")
        self.assertEqual(generate_soundex("Floor"), "F460")
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Rubin"), "R150")

    def test_generate_soundex_edge_cases(self):
        self.assertEqual(generate_soundex("Aaaa"), "A000")
        self.assertEqual(generate_soundex("A1"), "A000")
        self.assertEqual(generate_soundex("B2B"), "B100")
        self.assertEqual(generate_soundex("aBcD"), "A123")
        self.assertEqual(generate_soundex("XyZ"), "X200")
        self.assertEqual(generate_soundex("AEIOU"), "A000")
        self.assertEqual(generate_soundex("HWW"), "H000")
        self.assertEqual(generate_soundex("1234"), "1000")
        self.assertEqual(generate_soundex("A!@#$%^&*()"), "A000")
        self.assertEqual(generate_soundex("B1B2B3"), "B100")
        self.assertEqual(generate_soundex("Aaeiou"), "A000")
        self.assertEqual(generate_soundex("Baeiou"), "B000")

if __name__ == '__main__':
    unittest.main()
