class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = []
        for i in t:
            a.append(i)
        for j in s:
            if j in a:
                a.remove(j)
        return a[0]