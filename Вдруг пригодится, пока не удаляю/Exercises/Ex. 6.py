def int_to_str(i, base):
    if base > 36:
        raise ValueError(f'Invalid literal with base {base}')

    int_literals = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i',
                    19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r',
                    28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}

    number_list = []

    while i != 0:
        number_list.append(i % base)
        i = i // base
    number_list.reverse()

    for i, number in enumerate(number_list):
        number_list[i] = int_literals.get(number)

    output_string = ''
    for string in number_list:
        output_string += string

    return output_string
