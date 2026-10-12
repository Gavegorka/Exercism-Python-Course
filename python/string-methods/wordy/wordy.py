def answer(question):
    operation = question.lower().replace('?', '').split()

    for i, num in enumerate(operation):
        try:
            operation[i] = int(num)
        except ValueError:
            pass

    if not question.lower().startswith('what is ') or not question.endswith('?'):
        raise ValueError('syntax error')

    for i, item in enumerate(operation):
        if item == 'multiplied':
            operation[i] = '*'
        elif item == 'minus':
            operation[i] = '-'
        elif item == 'plus':
            operation[i] = '+'
        elif item == 'divided':
            operation[i] = '//'

    operation_clear = [
        item for item in operation
        if item not in ('what', 'is', 'by')
    ]

    if not operation_clear or len(operation_clear) % 2 == 0:
        if 'cubed' in operation_clear:
            raise ValueError('unknown operation')
        raise ValueError('syntax error')

    for i in range(len(operation_clear)):
        if i % 2 == 0:
            if not isinstance(operation_clear[i], int):
                if isinstance(operation_clear[i], str) and operation_clear[i] not in ('-', '+', '*', '//'):
                    raise ValueError('unknown operation')
                raise ValueError('syntax error')
        else:
            if operation_clear[i] not in ('-', '+', '*', '//'):
                if not isinstance(operation_clear[i], int):
                    raise ValueError('unknown operation')
                raise ValueError('syntax error')

    result = operation_clear[0]

    for i in range(1, len(operation_clear), 2):
        number = operation_clear[i + 1]

        if operation_clear[i] == '*':
            result *= number
        elif operation_clear[i] == '-':
            result -= number
        elif operation_clear[i] == '+':
            result += number
        elif operation_clear[i] == '//':
            result //= number

    return result