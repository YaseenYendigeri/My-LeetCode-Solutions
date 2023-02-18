class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        eA = list(range(1, len(nums)+1))
        r = list(set(eA) - set(nums))
        
        return r