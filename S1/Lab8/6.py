n = 6
x = [3, 29, 5, 5, 28, 6]
x.reverse()
# В этот массив заполняем наибольшую возр. подп. для каждого элемента
p = [0] * n
m = [0] * (n + 1)
l = 0

for i in range(n):
    left = 1
    right = l
    while left <= right:
        mid = (left + right) // 2
        if x[m[mid]] < x[i]:
            left = mid + 1
        elif x[m[mid]] == x[i]:
            left += 1
        else:
            right = mid - 1
    new_l = left
    p[i] = m[new_l - 1]

    if new_l > l:
        m[new_l] = i
        l = new_l
    elif x[i] < x[m[new_l]]:
        m[new_l] = i

print(p,m)
print(l)
k = m[l]
for i in range(l - 1, -1, -1):
    print(n - k, end=' ')
    k = p[k]