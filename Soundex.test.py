import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("M"), "M000")

    def test_two_characters(self):
        self.assertEqual(generate_soundex("MI"), "M000")
        self.assertEqual(generate_soundex("MB"), "M100")

    def test_three_characters(self):
        self.assertEqual(generate_soundex("ART"), "A630")
        self.assertEqual(generate_soundex("ABC"), "A120")

    def test_name_with_similar_sounding_letters(self):
        self.assertEqual(generate_soundex("Floor"), "F460")
        self.assertEqual(generate_soundex("Flower"), "F460")
        
    def test_name_with_varying_length(self):
        # Names shorter than 4 characters
        self.assertEqual(generate_soundex("Ml"), "M400")
        self.assertEqual(generate_soundex("Ro"), "R000")
        self.assertEqual(generate_soundex("Was"), "W200")

        # Names exactly 4 characters
        self.assertEqual(generate_soundex("Mass"), "M200")
        self.assertEqual(generate_soundex("Part"), "P630")
        self.assertEqual(generate_soundex("Rose"), "R200")

        # Names longer than 4 characters
        self.assertEqual(generate_soundex("Random"), "R535")
        self.assertEqual(generate_soundex("Parent"), "P653")
        self.assertEqual(generate_soundex("Customer"), "C235")




if __name__ == '__main__':
    unittest.main()
