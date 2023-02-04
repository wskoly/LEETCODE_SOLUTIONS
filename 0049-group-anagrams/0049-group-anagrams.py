class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        for word in strs:
            sorted_letter = "".join(sorted(word))
            if sorted_letter not in group_dict:
                group_dict[sorted_letter] = []
            group_dict[sorted_letter].append(word)
        return list(group_dict.values())
