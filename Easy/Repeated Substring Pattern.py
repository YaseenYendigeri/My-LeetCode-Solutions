class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = s+s
        n = n[1:-1]
        if s in n:
            return True
        else:
            return False