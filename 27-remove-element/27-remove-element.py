class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        found_val = 0
        for i in range(len(nums)):
            if nums[i] == val:
                found_val +=1
                continue
            nums[i-found_val] = nums[i]
            
        return len(nums)-found_val