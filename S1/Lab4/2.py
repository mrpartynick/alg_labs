def anti_quick_sort(n):

    l = []
    for i in range(1,n+1):
        l.append(i)

    l[len(l)//2], l[-1] = l[-1], l[len(l)//2]
    return l


def qsort(left, right):
    global a
    key = a [(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while a[i] < key:  # first while
            i += 1
        while a[j] > key:  # second while
            j -= 1
    if i <= j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    if left < j:
        qsort(left, j)
    if i < right:
        qsort(i, right)


a = anti_quick_sort(3)

i = qsort(0,len(a)-1)

print(a)