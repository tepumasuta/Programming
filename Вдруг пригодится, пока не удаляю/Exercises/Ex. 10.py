def convert_to_list(numbers: str):
    a = numbers.split(sep=",")
    for i in range(len(a)):
        a[i] = int(a[i])
    return a


def convert_to_tuple(numbers: str):
    return tuple(convert_to_list(numbers))

