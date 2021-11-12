def NextGreaterElement(A):
    n = len(A)
    B = [-1]*n
    S = []
    for i in range(n):
        # if len(S) == 0 or A[S[-1]] > A[i]:
        #     S.append(i)
        #     continue
        while len(S) and A[S[-1]] < A[i]:
            B[S[-1]] = A[i]
            S.pop()
        S.append(i)
    return B


if __name__ == "__main__":
    print(NextGreaterElement([6, 8, 0, 1, 3]))
    print(NextGreaterElement([11, 13, 21, 3]))
