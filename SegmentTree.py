import math


class SegmentTree:
    def __init__(self, arr) -> None:
        self.size = math.ceil(math.log2(len(arr)))
        self.S = [0] * self.size
        self.constructST(arr)

    def constructST(self, arr):
        self.constructSTUtil(0, arr, 0, len(arr))

    def constructSTUtil(self, si, arr, s, e):
        if s == e:
            self.S[si] = arr[s]
            return
        mid = (s+e)//2
        self.S[si] = self.constructSTUtil(
            2*si+1, arr, s, mid) + self.constructSTUtil(2*si+2, arr, mid+1, e)
        return

    def findSum(self, qs, qe):
        return self.findSumUtil(0, self.size-1, qs, qe, 0)

    def findSumUtil(self, ss, se, qs, qe, si):
        if ss >= qs and se <= qe:
            return self.S[si]
        if ss > qe or se < qs:
            return 0
        mid = (ss + se) // 2
        return self.findSumUtil(ss, se, qs, mid, 2*si+1) + self.findSumUtil(ss, se, mid+1, qe, 2*si+2)
