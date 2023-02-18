class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        return len(set(p)) == len(set(zip(p, s.split()))) == len(set(s.split())) and len(p) == len(s.split())
    