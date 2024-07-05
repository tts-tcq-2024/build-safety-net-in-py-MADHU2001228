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
    # Initialize the soundex code with the first letter
    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)

def should_add_code(char, code, prev_code):
    return code != '0' and code != prev_code

def add_code_to_soundex(soundex, code):
    return soundex + code

def is_length_four(soundex):
    return len(soundex) == 4

def process_characters(name, soundex, prev_code):
    # Generate codes and filter out '0' and codes that are the same as prev_code
    codes = filter(lambda code: code != '0' and code != prev_code, (get_soundex_code(char) for char in name[1:]))
    
    # Join the valid codes and take the first 3 characters
    soundex += ''.join(codes)[:3]
    
    return soundex

def pad_soundex(soundex):
    # Pad with zeros if necessary to ensure length is 4
    return soundex.ljust(4, '0')

def generate_soundex(name):
    if not name:
        return ""

    soundex, prev_code = initialize_soundex(name)
    soundex = process_characters(name, soundex, prev_code)
    return pad_soundex(soundex)
