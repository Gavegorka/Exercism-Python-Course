colors_lst = ['black', 'brown', 'red', 'orange', 'yellow',
              'green', 'blue', 'violet', 'grey', 'white']


def color_code(color):
    return colors_lst.index(color)


def value(colors):
    colors_code = str(color_code(colors[0])) + str(color_code(colors[1])) + '0' * color_code(colors[2])
    return int(colors_code)


def label(colors):
    resistance = value(colors)

    if resistance >= 1000000000:
        answer = str(resistance // 1000000000) + ' gigaohms'

    elif resistance >= 1000000:
        answer = str(resistance // 1000000) + ' megaohms'

    elif resistance >= 1000:
        answer = str(resistance // 1000) + ' kiloohms'
    else:
        answer = str(resistance) + ' ohms'
    return answer