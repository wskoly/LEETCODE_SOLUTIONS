import bisect, math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potions_len = len(potions)
        result = []
        for spell in spells:
            matched_range = math.ceil(success/spell)
            bisect_index = bisect.bisect_left(potions, matched_range)
            if bisect_index >= potions_len:
                count = 0
            else:
                count = potions_len-bisect_index
            result.append(count)
        return result