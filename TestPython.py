from collections import defaultdict
s = "abcdefghi"
print(s[::-1])

A = [1, 2, 4, 5, 6, 7, 9]

# for i in reversed(A):
#     print(i)

A.reverse()
# print(A)

s = "abcdefghi"
# print(s[1:4])
# print(s.split('d'))

B = [(1, 2, 3), (2, 3, 4), (2, 3, 1)]
C = sorted(B, key=lambda c: c[2])
# print(C)

D = {'a': 1, 'c': 3, 'b': 2}
E = sorted(D, key=lambda c: D[c])
print(E)
F = {}
