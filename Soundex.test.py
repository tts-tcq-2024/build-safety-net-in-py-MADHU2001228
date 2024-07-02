import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_two_characters(self):
        self.assertEqual(generate_soundex("AI"), "A000")
        self.assertEqual(generate_soundex("AB"), "A100")

    def test_three_characters(self):
        self.assertEqual(generate_soundex("ART"), "A630")
        self.assertEqual(generate_soundex("ARB"), "A610")

    def test_name_with_similar_sounding_letters(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")

    def test_name_with_varying_length(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    def test_name_with_non_alpha_characters(self):
        self.assertEqual(generate_soundex("H3llo"), "H400")
        self.assertEqual(generate_soundex("P@ul"), "P000")
        self.assertEqual(generate_soundex("O'Neill"), "O540")

if __name__ == '__main__':
    unittest.main()
