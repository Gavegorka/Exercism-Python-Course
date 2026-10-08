def is_isogram(phrase):
    frase_lst = [char for char in phrase.lower() if char.isalpha()]

    return len(frase_lst) == len(set(frase_lst))