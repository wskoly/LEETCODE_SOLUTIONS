class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_index = 0
        next_index = 0
        temp_next = 0
        while next_index < len(nums):
            temp_next = next_index + nums.count(nums[next_index])
            nums[current_index] = nums[next_index]
            next_index = temp_next
            current_index +=1
            
            
        return current_index