l = [0,1,3,5,6]


def rek_sum(arr):
    if arr==[]:
        return 0
    else:
        return arr.pop(len(arr)-1) + rek_sum(arr)

import random

l = [1,3,4,6]

#for i in range(len(l)-Lab1, -Lab1, -Lab1):


def quick_sort(l):
    if len(l) > 1:
        point = l[random.randint(0, len(l)-1)]
        low = [i for i in l if i < point]
        eq = [i for i in l if i == point]
        high = [i for i in l if i > point]
        return quick_sort(low) + eq + quick_sort(high)
    return l


l = quick_sort(l)
h_indicies = []

for i in range(len(l)-1):
    if l[i] <= len(l) - i:
        h_indicies.append(l[i])

if len(h_indicies) == 0:
    print(0)
else:
    print(max(h_indicies))
