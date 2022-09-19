import time

def merge_two_list(l1,l2):
    i = j = 0
    l3 = []
    if l1[-1] > l2[0]:
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
    else:
        return l1+l2

def merge_sort(l):
    if len(l) == 1:
        return l
    else:
        mid = len(l)//2
        left_part = merge_sort(l[:mid])
        right_part = merge_sort(l[mid:])
        return merge_two_list(left_part,right_part)

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

def choice_sort(l):
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                t = l[j]
                l[j] = l[i]
                l[i] = t
    return l

def time_of_sort(l):
    m_begin = time.perf_counter()
    merge_sort(l)
    m_end = time.perf_counter()
    m_time = m_end - m_begin

    i_begin = time.perf_counter()
    merge_sort(l)
    i_end = time.perf_counter()
    i_time = i_end - i_begin

    c_begin = time.perf_counter()
    merge_sort(l)
    c_end = time.perf_counter()
    c_time = c_end - c_begin

    return m_time, i_time, c_time

list_of_mid = []
# Записывает количество элементов, при которых мердж работает быстрее в массив и потом находит среднее из них
for n in range(1,11):
    result_list = []
    for i in range(10,100):
        l = [j for j in range(i,0,-1)]

        m_time, i_time, c_time = time_of_sort(l)

        if m_time < i_time and m_time < c_time:
            result_list.append(len(l))
    list_of_mid.append(sum(result_list)//len(result_list))

print(sum(list_of_mid)//len(list_of_mid))

