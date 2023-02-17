import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = list(heapq.merge(nums1,nums2))
        length = len(merged)
        if length%2 == 0:
            return (merged[length//2] + merged[(length//2)-1])/2
        return merged[length//2]