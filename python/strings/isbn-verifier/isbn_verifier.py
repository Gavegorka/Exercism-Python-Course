def is_valid(isbn):

    isbn_lst = []

    isbn = isbn.replace('-', '').strip()
    if len(isbn) != 10:
        return False
    i = 0
    for num in isbn:
        if num.isdigit():
            isbn_lst.append(int(num))
        elif num in ('x', 'X') and i == 9:
            isbn_lst.append(10)
        i +=1

    if len(isbn_lst) != 10:
        return False

    prove = 0
    i = 0
    for number in isbn_lst:
        prove += number * (10 - i)
        i += 1

    return prove % 11 == 0


print(is_valid('3-598-21508-9'))

