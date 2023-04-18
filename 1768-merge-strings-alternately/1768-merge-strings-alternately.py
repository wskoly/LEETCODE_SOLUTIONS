class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        out_str = ""
        for i in range(max_len):
            try:
                out_str += word1[i]
            except:
                pass
            try:
                out_str += word2[i]
            except:
                pass
        return out_str