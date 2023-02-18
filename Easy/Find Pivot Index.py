class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        psums = [0]
        for i in range(len(nums)):
            psums.append(psums[i] + nums[i]);

        for i in range(len(nums)):
            if psums[i] == psums[len(nums)] - psums[i+1]:
                return i;

        return -1;
        