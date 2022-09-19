def LCS_RECURSIVE(x, y):
    if len(x) == 0 or len(y) == 0:
        return []
    if x[-1] == y[-1]:
        return LCS_RECURSIVE(x[:-1], y[:-1]) + [x[-1]]
    else:
        left = LCS_RECURSIVE(x[:-1], y)
        right = LCS_RECURSIVE(x, y[:-1])
        return left if len(left) > len(right) else right

def solution(x,y):
    l = LCS_RECURSIVE(x,y)
    value = len(l)
    return value, l

print(solution([2,7,5,4,10], [2,5,4,15]))
