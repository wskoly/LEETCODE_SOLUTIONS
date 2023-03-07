class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        sol = []
        for i, num in enumerate(nums):
            j = i + 1
            k = len(nums)-1
            while j < k:
                if num+nums[j]+nums[k] > 0:
                    k -=1
                elif num+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    if [num, nums[j], nums[k]] not in sol:
                        sol.append([num, nums[j], nums[k]])
                    k -=1
                    j += 1
        return sol