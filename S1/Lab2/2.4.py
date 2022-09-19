def line_search():
    i_f = open("input.txt.txt", "r")
    o_f = open("output.txt", "w")
    l = []
    i = 0
    for line in i_f:
        for elem in line.split():
            l.append(int(elem))
    i_f.close()

    v = l.pop(-1)

    if v not in l:
        o_f.write(str(-1))
    else:
        for elem in l:
            if elem == v:
                o_f.write(str(i))
                o_f.write(" ")
            i += 1

    o_f.close()


line_search()