def MaxHistArea(A):
    n = len(A)
    S, area = [], 0
    for i in range(n):
        if len(S) == 0 or A[S[-1]] <= A[i]:
            S.append(i)
        else:
            while len(S) and A[S[-1]] > A[i]:
                area = max(area, (i-S[-1])*A[S[-1]])
                S.pop()
            S.append(i)

    while len(S):
        area = max(area, (n-S[-1])*A[S[-1]])
        S.pop()
    return area


a = MaxHistArea([2, 1, 5, 6, 2, 3])
a = MaxHistArea([2, 1, 2])
print(a)
