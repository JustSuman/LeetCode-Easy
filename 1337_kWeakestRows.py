class Solution:
    def kWeakestRows(self, mat, k):
        a = {}
        b = []
        key = []
        for i in range(0,len(mat)):
                x = mat[i].count(1)
                b.append(x)
                a[i]=x
        x = list(a.items())
        x.sort(key = lambda x : x[1])
        y = dict(x)
        for j in y.keys():
            key.append(j)
            if len(key)==k:
                break
        return (key)