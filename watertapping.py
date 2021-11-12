def watertapping(A):
    l = len(A)
    if l <= 2:
        return 0
    x, y = 1, l-2
    ml, mr = A[0], A[l-1]
    sum = 0
    while x <= y:
        if ml < mr:
            sum = sum + (ml-A[x]) if A[x] < ml else sum
            ml = max(ml, A[x])
            x += 1
        else:
            sum = sum + (mr-A[y]) if A[y] < mr else sum
            mr = max(mr, A[y])
            y -= 1
    return sum


if __name__ == '__main__':
    A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    x = watertapping(A)
    print(x)
