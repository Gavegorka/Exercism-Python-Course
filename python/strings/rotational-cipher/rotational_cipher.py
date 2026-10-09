import string as s

def rotate(text, key):

    lowercase_letters = s.ascii_lowercase
    uppercase_letters = s.ascii_uppercase
    result = ''
    for char in text:
        if char in lowercase_letters:
            result += lowercase_letters[(lowercase_letters.index(char) + key) % 26]
        elif char in uppercase_letters:
            result += uppercase_letters[(uppercase_letters.index(char) + key) % 26]
        else:
            result += char
    return result 