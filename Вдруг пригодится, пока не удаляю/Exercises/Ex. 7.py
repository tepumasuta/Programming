def pascal(n):
    if n < 1:
        raise ValueError(f"Invalid number of lines - {n}. It has to be greater than 0")
    if type(n) != int:
        raise ValueError(f"Invalid type of n. It has to be 'int'")

    output = []
    first_line = (1,)
    line = first_line

    for i in range(n):
        output.append(line)
        line = get_next_line(line)

    return output


def get_next_line(previous_line):
    next_line = []
    for i in range(len(previous_line) + 1):
        if i == len(previous_line):
            next_line.append(1)
        elif i == 0:
            next_line.append(1)
        else:
            next_line.append(previous_line[i - 1] + previous_line[i])
    return tuple(next_line)
