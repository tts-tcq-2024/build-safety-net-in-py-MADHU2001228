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


def generate_soundex(name):
    if not name:
        return ""

    soundex = name[0].upper()  # Start with the first letter (capitalized)
    prev_code = get_soundex_code(soundex)
    soundex_codes = [soundex]

    # Process remaining characters in the name
    for char in name[1:]:
        code = get_soundex_code(char)
        if len(soundex_codes) < 4 and code != '0' and code != prev_code:
            soundex_codes.append(code)
            prev_code = code

    # Pad with zeros if necessary to ensure length is 4
    return ''.join(soundex_codes).ljust(4, '0')


    return soundex
