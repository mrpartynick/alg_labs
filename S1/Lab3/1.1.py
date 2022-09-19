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
        return merge_two_list(left_part,right_part)

l = []
f = open("input.txt.txt", "r")

for line in f:
    for elem in line.split():
        l.append(int(elem))
f.close()
l = merge_sort(l[1:])

f = open("output.txt", "w")
for elem in l:
    f.write(str(elem))
    f.write(" ")
f.close()
