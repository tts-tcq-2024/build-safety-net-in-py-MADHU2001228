def get_soundex_code(c):
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c.upper(), '0')  # Default to '0' for non-mapped characters

def initialize_soundex(name):
    # Start with the first letter (capitalized)
    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)

def process_characters(name):
    soundex = ""
    prev_code = ""
    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
        if len(soundex) + 1 == 4:  # +1 to account for the first letter
            break
    return soundex

def pad_soundex(soundex):
    # Pad with zeros to ensure length of 4
    return soundex.ljust(4, '0')

def generate_soundex(name):
    if not name:
        return ""

    first_letter, initial_code = initialize_soundex(name)
    remaining_soundex = process_characters(name)
    soundex = first_letter + remaining_soundex

    return pad_soundex(soundex)


