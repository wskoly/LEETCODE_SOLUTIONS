class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if target == nums[mid]:
                is_found = True
                return mid
            elif target > nums[mid]:
                start = mid+1
            elif target < nums[mid]:
                end = mid-1
        return start
        