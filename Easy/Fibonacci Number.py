class Solution:
    def fib(self, n: int) -> int:
        def fib2(n):
            if n == 0 or n == 1:
                return n
            if n == 2:
                return 1
            else:
                return fib2(n-2)+fib2(n-1)
    
        return fib2(n)