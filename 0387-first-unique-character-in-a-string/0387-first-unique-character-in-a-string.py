class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrence_dict = {}
        for i, letter in enumerate(s):
            if letter not in occurrence_dict:
                occurrence_dict[letter] = [0]*2
            occurrence_dict[letter][0] += 1
            occurrence_dict[letter][1] = i

        for value in occurrence_dict.values():
            if value[0] == 1:
                return value[1]

        return -1