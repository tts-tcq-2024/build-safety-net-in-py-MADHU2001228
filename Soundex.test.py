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
        # Names shorter than 4 characters
        self.assertEqual(generate_soundex("Al"), "A400")
        self.assertEqual(generate_soundex("Bo"), "B000")
        self.assertEqual(generate_soundex("Lee"), "L000")

        # Names exactly 4 characters
        self.assertEqual(generate_soundex("John"), "J500")
        self.assertEqual(generate_soundex("Paul"), "P400")
        self.assertEqual(generate_soundex("Mark"), "M620")

        # Names longer than 4 characters
        self.assertEqual(generate_soundex("Smith"), "S530")
        self.assertEqual(generate_soundex("Johnson"), "J525")
        self.assertEqual(generate_soundex("Williams"), "W452")




if __name__ == '__main__':
    unittest.main()
