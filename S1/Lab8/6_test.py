n = 6
l = [3, 29, 5, 5, 28, 6]
#x.reverse()


def solution(n, x):
    # В этот массив заполняем наибольшую возр. подп. для каждого элемента
    value_about_position = [1] * n
    for i in range(n):
        if i == 0:
            continue
        if x[i] >= x[i-1]:
            value_about_position[i] = value_about_position[i-1] + 1

    a = value_about_position.index(max(value_about_position))
    result = x[len(value_about_position)-a:a+1]
    b = len(result)

    return b, result

print(solution(n,l))
