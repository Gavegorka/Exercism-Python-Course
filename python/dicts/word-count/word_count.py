separators = '.,;:!?…—–-()[]{}"«»„“/\&+*|=@$%^_'

def count_words(sentence):
    result ={}
    sent = sentence.lower()
    for char in sent:
        if char in separators:
            sent = sent.replace(char,' ')

    data = sent.split()
    for i, word in enumerate(data):
        data[i] = word.strip("'")
        if data[i]:
            if data[i] in result: result[data[i]] += 1
            else: result[data[i]] = 1
    return result