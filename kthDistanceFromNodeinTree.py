
def findAncestors(root, node, S):
    if root == None:
        return False
    if root == node:
        return True
    S.append(root)
    x = findAncestors(root.left, node, S)
    if x:
        return True
    S.pop()
    y = findAncestors(root.right, node, S)
    if y:
        return True
    S.pop()
    return False


def kthNode(root, k):
    if root == None:
        return [], False
    if k == 0:
        return [root], True
    l, x = kthNode(root.left, k-1)
    r, y = kthNode(root.right, k-1)
    out = []
    out = out + l if x else out
    out = out + r if y else out
    b = x or y
    return out, b


def kthDistanceFromNode(root, node, k):
    S = []
    x = findAncestors(root, node, S)
    out, _ = kthNode(node, k)
    while len(S):
        x = S.pop()
        y = S[-1]
        if x.left != y:
            l, _ = findAncestors(x.left, k-1)
        if x.right != y:
            r, _ = findAncestors(x.right, k-1)
        out = out + l + r
