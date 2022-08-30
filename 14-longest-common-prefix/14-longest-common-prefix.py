class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """    
        longest_prefix = ""
        for letter in strs[0]:
            has_letter = True
            for s in strs:
                if not s.startswith(longest_prefix+letter):
                    has_letter = False
                    break
            if not has_letter:
                break
            longest_prefix += letter
            
        return longest_prefix
        