# В этот словарь мы записываем пары число-кортеж. Число обозначает, собственно, само число, а в кортежи хранятся числа
# Из которых можно прийти в это число.
d = {}

# Функция, которая заполняет словарь
def f(n):
    if n == 1:
        return 1, -1
    if d.get(n) is not None:
        return d[n]
    ans = (f(n - 1)[0] + 1, n - 1)

    if n % 2 == 0:
        ret = f(n // 2)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 2)

    if n % 3 == 0:
        ret = f(n // 3)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 3)

    d[n] = ans
    return ans

# Функция, которая выводит на печать.
def print_solution(n):
    ans = []
    ans.append(n)
    n -= 1

    while True:
        if n == 1:
            break
        ans.append(n)
        n = d[n][1]

    ans.append(1)
    ans.reverse()
    print(len(ans)-1)
    print(*ans)

def solve(n):
    for i in range(1, n):
        f(i)
    print_solution(n)
    print('')

solve(5)

