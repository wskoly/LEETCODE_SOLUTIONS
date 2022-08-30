public class Solution {
    public int[] TwoSum(int[] nums, int target)
        {
             int target_mid = (int)target / 2;
            int closest_target_mid = 0;
            int[] sorted_nums = new int[nums.Length];
            for (int k = 0; k < nums.Length; k++)
            {
                if (target_mid > 0)
                {
                    if (nums[k] <= target_mid && (target_mid - nums[k]) < (target_mid - closest_target_mid))
                    {
                        closest_target_mid = nums[k];
                    }
                }
                else
                {
                    if (nums[k] >= target_mid && (target_mid - nums[k]) > (target_mid - closest_target_mid))
                    {
                        closest_target_mid = nums[k];
                    }
                }
                sorted_nums[k] = nums[k];
            }
            Array.Sort(sorted_nums);
            if(closest_target_mid == 0) closest_target_mid = nums[nums.Length-1];
            int closest_target_mid_index = Array.IndexOf(sorted_nums, closest_target_mid);

            int first_index = -1;
            int second_index = -1;
            int remain_value = -99;
            for (int i = closest_target_mid_index; i >= 0; i--)
            {
                first_index = Array.IndexOf(nums, sorted_nums[i]);
                remain_value = target - sorted_nums[i];
                second_index = (remain_value == sorted_nums[i]) ? Array.LastIndexOf(nums, remain_value) : Array.IndexOf(nums, remain_value);

                if (second_index >= 0 && second_index != first_index)
                {
                    break;
                }

            }
        
            int[] result = { first_index, second_index };
            Array.Sort(result);
            return result;
        }
}