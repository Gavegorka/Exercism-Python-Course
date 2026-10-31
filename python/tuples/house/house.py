objects = [
    "the house that Jack built",
    "the malt",
    "the rat",
    "the cat",
    "the dog",
    "the cow with the crumpled horn",
    "the maiden all forlorn",
    "the man all tattered and torn",
    "the priest all shaven and shorn",
    "the rooster that crowed in the morn",
    "the farmer sowing his corn",
    "the horse and the hound and the horn"
]

actions = [
    None,
    "that lay in",
    "that ate",
    "that killed",
    "that worried",
    "that tossed",
    "that milked",
    "that kissed",
    "that married",
    "that woke",
    "that kept",
    "that belonged to"
]

def recite(start_verse, end_verse):
    result = [f'{objects[0]}']
    for i in range (1, end_verse):
        verse = f'{objects[i]} {actions[i]} ' + result[-1]
        result.append(verse)
    answer = [f'This is {item}.' for item in result]

    return answer[start_verse -1:end_verse]