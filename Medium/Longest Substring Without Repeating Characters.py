class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        st = 0
        m = 0
        for i, ch in enumerate(s):
            if ch not in c:
                c.add(ch)
            else:
                m = len(c) if m < len(c) else m
                while(s[st]!= ch):
                    c.remove(s[st])
                    st+=1
                st+=1
        m = len(c) if m<len(c) else m
        return m