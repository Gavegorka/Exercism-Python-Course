days = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
presents ={
    1 : 'a Partridge in a Pear Tree',
    2: 'two Turtle Doves',
    3: 'three French Hens',
    4: 'four Calling Birds',
    5: 'five Gold Rings',
    6: 'six Geese-a-Laying',
    7: 'seven Swans-a-Swimming',
    8: 'eight Maids-a-Milking',
    9: 'nine Ladies Dancing',
    10: 'ten Lords-a-Leaping',
    11: 'eleven Pipers Piping',
    12: 'twelve Drummers Drumming'
}

def recite(start_verse, end_verse):
    result_lst = []
    for num_day in range(start_verse, end_verse + 1):
        result = f'On the {days[num_day]} day of Christmas my true love gave to me: '
        if num_day == 1:
            result += 'a Partridge in a Pear Tree.'
        else:
            for present in range(num_day, 1, -1):
                result += f'{presents[present]}, '
            result += 'and a Partridge in a Pear Tree.'
        result_lst.append(result)
    return result_lst