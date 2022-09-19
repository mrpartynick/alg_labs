def counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result


l = [5,2,3,17,10,11]

print(counting_sort(l,17))
