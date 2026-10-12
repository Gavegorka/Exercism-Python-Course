def commands(binary_str):
    binary_lst = [int(i) for i in binary_str]
    handshake = []
    if binary_lst[4] == 1:
        handshake.append('wink')
    if binary_lst[3] == 1:
        handshake.append('double blink')
    if binary_lst[2] == 1:
        handshake.append('close your eyes')
    if binary_lst[1] == 1:
        handshake.append('jump')
    if binary_lst[0] == 1:
        return handshake[::-1]
    return handshake
