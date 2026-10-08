def translate(text):
    return ' '.join(pig_latin(word) for word in text.split())


def pig_latin(word):
    vowels = 'aeiou'
    cons_in_beg = 0
    
    for char in word:
        if char in 'aeiou' or char == 'y':
            break
        else:
            cons_in_beg += 1
            
    if word[0] in vowels or word[:2] in ('xr', 'yt'):
        return word + 'ay'

    if cons_in_beg > 0 and word.startswith('qu', cons_in_beg - 1):
        return word[cons_in_beg + 1:] + word[:cons_in_beg - 1] + 'quay'

    if word.startswith('y'):
        return word[cons_in_beg + 1:] + word[:cons_in_beg + 1] + 'ay'
        
    if cons_in_beg > 0 and word.startswith('y', cons_in_beg):
        return word[cons_in_beg:] + word[:cons_in_beg] + 'ay'
    
    if cons_in_beg > 0:
        return word[cons_in_beg:] + word[:cons_in_beg] + 'ay'
