prior = {'6':['7', '8', '9', 'T', 'J', 'Q', 'K', 'A'],
 '7':['8', '9', 'T', 'J', 'Q', 'K', 'A'],
 '8':['9', 'T', 'J', 'Q', 'K', 'A'],
 '9':['T', 'J', 'Q', 'K', 'A'],
 'T':['J', 'Q', 'K', 'A'],
 'J':['Q', 'K', 'A'],
 'Q':['K', 'A'],
 'K':['A'],
 'A':[None],
 'koz':['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']}
f = open('input.txt', 'r')
n, m, koz = f.readline().split()
n, m = int(n), int(m)
cards = list(map(str, f.readline().split()))
cards_b = list(map(str, f.readline().split()))
d = open('output.txt', 'w')
S, C, D, H = [], [], [], []
for i in range(n):
    m1 = cards[i][1]
    n1 = cards[i][0]
    if m1 == 'S':
        S.append(n1)
    elif m1 == 'C':
        C.append(n1)
    elif m1 == 'D':
        D.append(n1)
    elif m1 == 'H':
        H.append(n1)
for i in range(m):
    flag = False
    num = cards_b[i][1]
    mast = cards_b[i][0]
    if num == 'S':
        for j in prior[mast]:
            if flag == False:
                if j in S:
                    S.remove(j)
                    flag = True
    elif num == 'C':
        for j in prior[mast]:
            if flag == False:
                if j in C:
                    C.remove(j)
                    flag = True
    elif num == 'D':
        for j in prior[mast]:
            if flag == False:
                if j in D:
                    D.remove(j)
                    flag = True
    elif num == 'H':
        for j in prior[mast]:
            if flag == False:
                if j in H:
                    H.remove(j)
                    flag = True
    if flag == False:
        if num == koz:
            d.write('NO')
            exit()
    else:
        if koz == 'S':
            for j in prior['koz']:
                if flag == False:
                    if j in S:
                        S.remove(j)
                        flag = True
        elif koz == 'C':
            for j in prior['koz']:
                if flag == False:
                    if j in C:
                        C.remove(j)
                        flag = True
        elif koz == 'D':
            for j in prior['koz']:
                if flag == False:
                    if j in D:
                        D.remove(j)
                        flag = True
        elif koz == 'H':
            for j in prior['koz']:
                if flag == False:
                    if j in H:
                        H.remove(j)
                        flag = True
        if flag == False:
            d.write('NO')
            exit()
d.write('YES')