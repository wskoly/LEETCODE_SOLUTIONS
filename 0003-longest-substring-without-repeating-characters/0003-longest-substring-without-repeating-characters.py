class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_so_far, current_max, i = 0, 0, 0
        unique_map = {}
        while i < len(s):
            if s[i] not in unique_map:
                unique_map[s[i]] = i
                current_max += 1
                i += 1
                continue
            if current_max >  max_so_far:
                max_so_far = current_max
            current_max = 0
            i = unique_map[s[i]] + 1
            unique_map = {}
        return max_so_far if max_so_far > current_max else current_max