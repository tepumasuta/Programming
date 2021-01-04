import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}


def dict_sort1(dictionary):
    return dict(sorted(dictionary.items(), key=operator.itemgetter(1)))


def dict_sort2(dictionary):
    items = list(dictionary.items())
    values = list(dictionary.values())
    tmp_dict = {}

    for key, value in items:
        tmp_dict.setdefault(value, key)

    values.sort()
    output_dict = {}
    for value in values:
        output_dict.setdefault(tmp_dict.get(value), value)

    return output_dict


print(dict_sort1(d), dict_sort2(d), sep="\n\n")
