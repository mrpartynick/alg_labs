def get(x):
    global table
    if x in table:
        return table[x][1]
    return '<none>'

def prev(x):
    global table
    if x in table:
        return get(table[x][0])
    return '<none>'

def next(x):
    global table
    if x in table:
        return get(table[x][2])
    return '<none>'

def put(x, y):
    global table
    if x in table:
        table[x][1] = y
    else:
        global bef
        table[bef][2] = x
        table[x] = [bef, y, '<none>']
        bef = x

def delete(x):
    global table
    if x in table:
        global bef
        if x == bef:
            if table[x][0] != '<none>':
                bef = table[x][0]
        if table[x][0] != '<none>':
            table[table[x][0]][2] = table[x][2]
        if table[x][2] != '<none>':
            table[table[x][2]][0] = table[x][0]
        del(table[x])



N = int(input())
itog = []
table = {}
bef = ''
for i in range(N):
    com = list(input().split())
    if com[0] == 'put':
        if len(table) == 0:
            table[com[1]] = ['<none>', com[2], '<none>']
            bef = com[1]
        else:
            put(com[1], com[2])
    elif com[0] == 'get':
        itog.append(get(com[1]))
    elif com[0] == 'prev':
        itog.append(prev(com[1]))
    elif com[0] == 'next':
        itog.append(next(com[1]))
    else:
        delete(com[1])
print('\n'.join(itog))
