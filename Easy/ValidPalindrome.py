class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', ' '] 
        for i in s:
             if i not in symbols:
                 new_str+=i.lower()

        if new_str == new_str[::-1]:
            return True
        return False

        

        