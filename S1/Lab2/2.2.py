def read_information_from_file():
    l = []
    f = open("input.txt.txt", "r")
    for line in f:
        for elem in line.split():
            l.append(int(elem))
    f.close()
    return l[1:]

def write_in_file(ar1, ar2):
    f = open("output.txt", "w")
    for elem in ar1:
        f.write(str(elem))
        f.write(" ")
    f.write("\n")
    for elem in ar2:
        f.write(str(elem))
        f.write(" ")

def insertion_sort():
    l = read_information_from_file()
    index_list = [1]

    for i in range(0,len(l)):
        for j in range(i,0,-1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
                if j-1 == 0:
                    index_list.append(1)
            else:
                index_list.append(j + 1)
                break
    write_in_file(index_list, l)

insertion_sort()