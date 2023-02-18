class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        v = 0
        ans = []
        index = 0
        
        for i in range(0, len(s)):
            if i == 0:
                v+=1
                continue
            elif s[i] == '(':
                v+=1
            else:
                v-=1
            if v == 0:
                ans.append(s[index:i+1])
                index = i+1
                
        t = ''
        for i in ans:
            n = len(i)
            t+=i[1:n-1]
        
        return t
        
        