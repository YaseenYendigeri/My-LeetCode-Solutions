class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = nums1+nums2
        k.sort()
        mid = len(k)//2
        res = (k[mid] + k[~mid])/2

        return res