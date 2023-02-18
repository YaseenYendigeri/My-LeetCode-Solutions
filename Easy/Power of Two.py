class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        flag = 0
        for i in range(0,32):
            if n == 2**i:
                flag = 1
        
        if flag == 1:
            return True
        else:
            return False
        