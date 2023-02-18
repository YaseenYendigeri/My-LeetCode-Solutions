class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            n = nums[i]
            if n>=10 and n<=99 or n>=1000 and n<=9999 or n==100000:
                count+=1
        return count