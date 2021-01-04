a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


#  1
def intersections_of_lists1(a, b):
    tmp_a = a.copy()
    tmp_b = b.copy()
    has_intersections = True
    output_list = []

    while has_intersections:
        has_intersections = False
        for i in tmp_a:
            for j in tmp_b:
                if i == j:
                    output_list.append(i)
                    tmp_a.remove(i)
                    tmp_b.remove(j)
                    has_intersections = True
    return output_list


#  2
def intersections_of_lists2(*args):
    output_list = []
    args = list(args)

    while args != [] and len(args) > 1:
        a = args.pop(len(args) - 1).copy()
        b = args[len(args) - 2].copy()

        has_intersections = True

        while has_intersections:
            has_intersections = False
            for i in a:
                for j in b:
                    if i == j:
                        output_list.append(i)
                        a.remove(i)
                        b.remove(j)
                        has_intersections = True
    return output_list


#  3
def intersections_of_lists3(*args):
    if not args:
        return []
    args = [set(i) for i in args]
    output_list = args.pop()

    for i in args:
        output_list.intersection_update(i)
    return list(output_list)


print(intersections_of_lists1(a, b), end="\n\n")
print(intersections_of_lists2(a, b), end="\n\n")
print(intersections_of_lists3(a, b))
