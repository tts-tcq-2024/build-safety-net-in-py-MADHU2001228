import unittest
from Soundex import generate_soundex
from Soundex import get_soundex_code 

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

        self.assertEqual(generate_soundex("Part"), "P630")
        self.assertEqual(generate_soundex("Rose"), "R200")

        # Names longer than 4 characters
        self.assertEqual(generate_soundex("Random"), "R535")
        self.assertEqual(generate_soundex("Parent"), "P653")
        
    def test_name_with_repeating_characters(self):
        self.assertEqual(generate_soundex("Maaa"), "M000")
        self.assertEqual(generate_soundex("Nbbb"), "N100")

    def test_name_with_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("A1"), "A000")
        self.assertEqual(generate_soundex("B2R"), "B600")
        self.assertEqual(generate_soundex("A!@#$%^&*()"), "A000")

    def test_name_with_numbers_only(self):
        self.assertEqual(generate_soundex("1234"), "1000")

    def test_get_soundex_code(self):
        # Test for '1' mappings
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('F'), '1')
        self.assertEqual(get_soundex_code('P'), '1')
        self.assertEqual(get_soundex_code('V'), '1')
        
        # Test for '2' mappings
        self.assertEqual(get_soundex_code('C'), '2')
        self.assertEqual(get_soundex_code('G'), '2')
        self.assertEqual(get_soundex_code('J'), '2')
        self.assertEqual(get_soundex_code('K'), '2')
        self.assertEqual(get_soundex_code('Q'), '2')
        self.assertEqual(get_soundex_code('S'), '2')
        self.assertEqual(get_soundex_code('X'), '2')
        self.assertEqual(get_soundex_code('Z'), '2')

        # Test for '3' mappings
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('T'), '3')

        # Test for '4' mapping
        self.assertEqual(get_soundex_code('L'), '4')

        # Test for '5' mappings
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('N'), '5')

        # Test for '6' mapping
        self.assertEqual(get_soundex_code('R'), '6')

        # Test for characters that should return '0'
        self.assertEqual(get_soundex_code('H'), '0')
        self.assertEqual(get_soundex_code('W'), '0')
        self.assertEqual(get_soundex_code('A'), '0')
        self.assertEqual(get_soundex_code('E'), '0')
        self.assertEqual(get_soundex_code('I'), '0')
        self.assertEqual(get_soundex_code('O'), '0')
        self.assertEqual(get_soundex_code('U'), '0')
        self.assertEqual(get_soundex_code('Y'), '0')
        self.assertEqual(get_soundex_code('1'), '0')
        self.assertEqual(get_soundex_code('*'), '0')





if __name__ == '__main__':
    unittest.main()
