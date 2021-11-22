def read_data(filename):
    f = open(filename, "r")
    file = f.readline()
    file = file.split(" ")
    i = 0
    while i < len(file):
        file[i] = int(file[i])
        i += 1
    return file


def is_in_linear(val, values):
    i = 0
    while i < len(values):
        if val == values[i]:
            return True
        i += 1
    return False