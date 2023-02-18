class Solution:
    def runningSum(self, l: List[int]) -> List[int]:
        l2 = []
        for i in range(len(l)):
            if i==0:
                l2.append(l[i])
            else:
                l[i] = l[i-1]+l[i]
                l2.append(l[i])
    
        return l2