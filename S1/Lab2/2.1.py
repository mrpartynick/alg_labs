def read_information_from_file():
    l = []
    f = open("input.txt.txt", "r")
    for line in f:
        for elem in line.split():
            l.append(int(elem))
    f.close()
    return l[1:]


def insertion_sort():
    l = read_information_from_file()

    for i in range(0, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break
    f = open("output.txt", "w")
    for elem in l:
        f.write(str(elem))
        f.write(" ")
    f.close()
