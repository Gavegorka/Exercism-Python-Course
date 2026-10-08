"""Determine what Bob will reply."""


def response(hey_bob):

    """
    Function determines what Bob will reply

    Args:
        hey_bob (str) - message to Bob

    Returns:
        str - Bob's reply

    Rules:
        "Sure." This is his response if you ask him a question, such as "How are you?"
            The convention used for questions is that it
        ends with a question mark.

        "Whoa, chill out!"
            This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.

        "Calm down, I know what I'm doing!"
            This is what he says if you yell a question at him.

        "Fine. Be that way!"
            This is how he responds to silence.
            The convention used for silence is nothing, or various combinations
            of whitespace characters.

        "Whatever." This is what he answers to anything else.
    """
    
    hey_bob = hey_bob.strip()
    
    cond_question = hey_bob.endswith('?')
    cond_yell = hey_bob == hey_bob.upper()
    cond_silence = hey_bob == ''
    cond_letters = any(char.isalpha() for char in hey_bob)

    if cond_silence:
        return 'Fine. Be that way!'
    elif cond_letters:
        if cond_question and not cond_yell:
            return 'Sure.'
        elif not cond_question and cond_yell:
            return 'Whoa, chill out!'
        elif cond_question and cond_yell:
            return "Calm down, I know what I'm doing!"
    else:
        if cond_question:
            return 'Sure.'

    return 'Whatever.'