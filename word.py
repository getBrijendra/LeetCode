def findWord1(A):
    F = {}
    B = {}
    for i in A:
        t = i.split('>')
        F.update({t[0]: t[1]})
        B.update({t[1]: t[0]})

    w = ''

    #for i in F.keys():
    k = F.keys()
    for x in F.keys():
        i = x
        w = i
        break
    #w = i
    while len(w) != len(F.keys()) + 1:
        if F.get(i) != None:
            w = w + F[i]
            i = F[i]
        else:
            i = B.get(i)
            continue

    return w

def findWord2(A):
    F = {}
    V = {}
    for i in A:
        t = i.split('>')
        F.update({t[0]: t[1]})
        V.update({t[0]: False})
      
    w = []
    for x in V.keys():
        if V.get(x) == False:
            Visit(F, V, x, w)
    return w

def Visit(F, V, k, w):
    if V.get(k) == False:
        V[k] = True
        if F.get(k) != None:
            k = F[k] 
            Visit(F, V, k, w)
    w.append(k)  
    return 

def findWord(A):
    F = {}
    for i in A:
        t = i.split('>')
        F.update({t[0]: t[1]})

    k = set(F.keys())
    v = set(F.values())
    start = ''
    for i in k:
        if (i in v ) == False:
            start = i
    w = start 
    while len(w) != len(A)+1:
        if F.get(start) != None:
            w = w + F.get(start)
            start = F.get(start)
    return w


print(findWord(["P>E","E>R","R>U"]))
print(findWord(["E>R","R>U", "P>E", "U>T"]))