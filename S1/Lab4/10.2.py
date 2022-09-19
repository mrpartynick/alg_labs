import random
l = [10,7,15,0]


def median_element(l):
    first = l[0]
    mid = l[len(l)//2]
    last = l[-1]
    return (first + mid + last)//3


def quick_sort(l):
    if len(l) > 1:
        point = median_element(l)
        low = [i for i in l if i < point]
        eq = [i for i in l if i == point]
        high = [i for i in l if i > point]
        return quick_sort(low) + eq + quick_sort(high)
    return l


print(quick_sort(l))