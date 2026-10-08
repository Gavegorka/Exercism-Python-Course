def is_pangram(sentence):

    letters = {char for char in sentence.lower() if char.isalpha()}
    
    return letters == set("abcdefghijklmnopqrstuvwxyz")
