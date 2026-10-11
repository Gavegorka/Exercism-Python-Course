pairs = {')': '(', ']': '[', '}': '{'}


def is_paired(input_string):
    stack = []
    for symb in input_string:
        if symb in ('[', '{', '('):
            stack.append(symb)
        elif symb in (']', '}', ')'):
            if stack == []:
                return False
            elif pairs[symb] != stack[-1]:
                return False
            else:
                stack.pop(-1)
        else:
            continue
    return stack == []