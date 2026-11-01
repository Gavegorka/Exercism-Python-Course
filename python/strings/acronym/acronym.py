def abbreviate(words):
    result = ''
    for char in range(len(words)):
        if char == 0 and words[char].isalpha():
            result += words[char].upper()
        elif words[char].isalpha() and words[char-1] in (' ', '-', '_'):
            result += words[char].upper()
    return result