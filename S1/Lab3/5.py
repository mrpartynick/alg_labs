#Сортируем по возрастанию. Разбиваем изначальный массив на подмассивы из его элементов, находим максимальный подмассив
#И сравниваем его длину с длиной массива пополам. Короче нужна максимальная подпоследовательность.

def merge_two_list(l1,l2):
    i = j = 0
    l3 = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1

    while j < len(l2):
        l3.append(l2[j])
        j += 1

    while i < len(l1):
        l3.append(l1[i])
        i += 1
    return l3

def merge_sort(l):
    if len(l) == 1:
        return l
    else:
        mid = len(l)//2
        left_part = merge_sort(l[:mid])
        right_part = merge_sort(l[mid:])
        return merge_two_list(left_part, right_part)

l = [2,3,3,9,2,2,2]

l = merge_sort(l)

def rek_sum(arr):
    if arr == []:
        return 0
    else:
        return a.pop(0) + rek_sum(arr)

half_of_l = l[len(l)//2+1]

if half_of_l[0] == half_of_l[-1] and half_of_l[-1] == l[half_of_l:]:
    print(1)
else:
    print(0)


