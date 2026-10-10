colors_lst = ['black', 'brown', 'red', 'orange', 'yellow',
              'green', 'blue', 'violet', 'grey', 'white']
tolerance = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5, 'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}

def color_code(color):
    return colors_lst.index(color)


def value(colors):
    if len(colors) == 1:
        colors_code = 0
    if len(colors) == 4:
        colors_code = str(color_code(colors[0])) + str(color_code(colors[1])) + '0' * color_code(colors[2])
    if len(colors) == 5:
        colors_code = str(color_code(colors[0])) + str(color_code(colors[1])) + str(color_code(colors[2])) + '0' * color_code(colors[3])
    return int(colors_code)


def resistor_label(colors):
    resistance = value(colors)
    if len(colors) == 1:
        return '0 ohms'
    if resistance >= 1000000000:
        if (resistance / 1000000000) % 1 == 0:
            answer = str(resistance // 1000000000) + ' gigaohms'
        else:
            answer = str(resistance / 1000000000) + ' gigaohms'
    elif resistance >= 1000000:
        if (resistance / 1000000) % 1 == 0:
            answer = str(resistance // 1000000) + ' megaohms'
        else:
            answer = str(resistance / 1000000) + ' megaohms'
    elif resistance >= 1000:
        if (resistance / 1000) % 1 == 0:
            answer = str(resistance // 1000) + ' kiloohms'
        else:
            answer = str(resistance / 1000) + ' kiloohms'
    else:
        answer = str(resistance) + ' ohms'

    return answer + " ±" + str(tolerance[colors[-1]]) + '%'
