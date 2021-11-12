def longestCommonPrefix(strs) -> str:
    V = [True]*len(strs[0])
    for i in range(1, len(strs)):
        ml = min(len(strs[0]), len(strs[i]))
        if len(V) > ml:
            V[ml] = False
        for j in range(ml):
            if V[j] == False:
                break
            if strs[0][j] != strs[i][j]:
                V[j] = False
                break

    c = 0
    for i in V:
        if i == False:
            break
        c += 1

    return strs[0][:c]


print(longestCommonPrefix(["as", "abc"]))
