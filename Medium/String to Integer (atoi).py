class Solution:
    def myAtoi(self, s: str) -> int:
        l, m = -2**31, 2**31-1
        n, emt, sign = 0, True, 1
        
        for c in s:
            if emt:
                if c == " ":continue
                elif c == "-":sign = -1
                elif c.isdigit():n = int(c)
                elif c!='+':return 0
                emt = False
            else:
                if c.isdigit():
                    n = n*10+int(c)
                    if sign*n>m:return m
                    elif sign*n<l:return l
                else:
                    break
        
        return sign*n
        