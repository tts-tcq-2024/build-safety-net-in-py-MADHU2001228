def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def initialize_soundex(name):
    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)

def process_characters(name, prev_code):
    # Generate codes for characters in the name starting from the second character
    codes = (get_soundex_code(char) for char in name[1:])
    # Filter out '0' codes and consecutive duplicates
    filtered_codes = (code for code in codes if code != '0' and code != prev_code)
    return ''.join(filtered_codes)[:3]  # Take the first 3 valid codes

def pad_soundex(soundex):
    return soundex.ljust(4, '0')

def generate_soundex(name):
    if not name:
        return ""

    soundex, prev_code = initialize_soundex(name)
    soundex += process_characters(name, prev_code)
    return pad_soundex(soundex)
