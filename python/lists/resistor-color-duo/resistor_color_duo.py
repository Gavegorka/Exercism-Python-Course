colors_lst = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]

def color_code(color):
    return colors_lst.index(color)

def value(colors):
    colors_code = int(str(color_code(colors[0])) + str(color_code(colors[1])))
    return colors_code

