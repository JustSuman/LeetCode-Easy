class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = []
        m = []
        for j in magazine:
            m.append(j)
        for i in ransomNote:
            n.append(i)
            print(n)
            if i in m:
                n.remove(i)
                m.remove(i)
                print(n)
            else:
                return False
        if not n:
            return True
        else:
            return False