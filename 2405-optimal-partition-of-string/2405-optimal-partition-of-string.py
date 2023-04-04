class Solution:
    def partitionString(self, s: str) -> int:
        substrings = []
        prev = ""
        for letter in s:
            if letter in prev:
                substrings.append(prev)
                prev = letter
                continue
            prev += letter
        substrings.append(prev)
        return len(substrings)