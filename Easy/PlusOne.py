class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = []
        k = int("".join(map(str, digits)))
        k+=1
        s = str(k)
        for i in s:
            l.append(int(i))
        
        return l