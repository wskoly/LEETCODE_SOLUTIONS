class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_index = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[current_index-1]:
                continue
            nums[current_index] = nums[i]
            current_index += 1

        return current_index
        