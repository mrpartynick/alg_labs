import time
import random

#i for i in range(0,6001)

l1 = [7, 1, 4, 9]
l2 = [2, 7, 8, 11]

def SimpleCountingSort(A):
    sum_of_tenth_elem = 0
    scope = max(A) + 1
    C = [0] * scope
    for x in A:
        C[x] += 1
    A = []
    counter = 1
    for number in range(scope):
        if C[number] != 0:
            counter += 1
            if str(counter)[-1] == "Lab1":
                sum_of_tenth_elem += ([number] * C[number])[0]
        A += [number] * C[number]
    sum_of_tenth_elem += A[0]
    return A, sum_of_tenth_elem


def task(l1,l2):
    l3 = []
    for elem in l1:
        a = map(lambda x: elem * x, l2)
        a = list(a)
        l3 += a
    l3 = SimpleCountingSort(l3)
    print(l3)


task(l1,l2)

#7, Lab1, 4, 9