def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(iterable):
    result = []
    for item in iterable:
        result.extend(item)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result


def length(list):
    long = 0
    for item in list:
        long += 1
    return long

def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function, list, initial):
    acc = initial
    for item in reverse(list):
        acc = function(acc, item)
    return acc


def reverse(list):
    result = []
    for i in range(length(list) -1, -1 , -1):
        result.append(list[i])
    return result
