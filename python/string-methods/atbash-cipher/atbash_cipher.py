alphabet = "abcdefghijklmnopqrstuvwxyz"
mirror = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    str_clean = ''.join(char for char in plain_text.lower() if char.isalnum())
    ciphered = []
    for char in str_clean:
        if char.isalpha():
            ciphered.append(alphabet[-alphabet.index(char) - 1])
        else:
            ciphered.append(char)
    ciphered_str = ''.join(ciphered)
    return ' '.join(ciphered_str[i:i+5] for i in range(0, len(ciphered_str), 5))

    
def decode(ciphered_text):
    str_clean_cip = ''.join(char for char in ciphered_text.lower() if char.isalnum())
    unciphered = []
    for char in str_clean_cip:
        if char.isalpha():
            unciphered.append(mirror[-mirror.index(char) - 1])
        else:
            unciphered.append(char)
    unciphered_str = ''.join(unciphered)
    return unciphered_str
