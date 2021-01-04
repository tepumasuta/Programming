import operator

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}


def get_3maxvalue_keys(d):
    items = d.items()
    tmp_list = []

    i = len(items)
    for key, value in sorted(items, key=operator.itemgetter(1)):
        if i <= 3:
            tmp_list.append(key)
        i -= 1

    return tmp_list


print(get_3maxvalue_keys(my_dict))
