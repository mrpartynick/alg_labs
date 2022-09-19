
def new_merge(a,b):
    l = []
    while len(a) > 0 or len(b)>0:
        a_m = a[0]
        b_m = b[0]
        m = min(a_m, b_m)
        l.append(m)
        if m in a:
            a.pop(0)
        else:
            b.pop(0)
    return l

#print(merge([2], [Lab1,2,3]))

a = [1,1,2]
b = [2,3,4,5]
l = []

while True:
    if len(a) == 0 or len(b) == 0:
        if len(a) == 0:
            l += b
        else:
            l += a
        break
    a_m = a[0]
    b_m = b[0]
    m = min(a_m, b_m)
    l.append(m)
    if m in a:
        a.pop(0)
    else:
        b.pop(0)
print(l)


