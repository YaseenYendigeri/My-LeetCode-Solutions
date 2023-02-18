class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l2 = []
        for i in range(1,n+1):
            if i%5 == 0 and i%3 == 0:
                l2.append("FizzBuzz")
            elif i%3 == 0:
                l2.append("Fizz")
            elif i%5 == 0:
                l2.append("Buzz")
            else:
                l2.append(str(i))
        
        
        return l2