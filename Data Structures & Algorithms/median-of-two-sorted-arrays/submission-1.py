class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalL = len(nums1) + len(nums2)
        merged = nums1 + nums2
        merged.sort()

        totallen = len(merged)
        if totallen % 2 == 0:
            return(merged[totallen//2 -1] + merged[totallen//2]) / 2.0
        else:
            return merged[totallen // 2]