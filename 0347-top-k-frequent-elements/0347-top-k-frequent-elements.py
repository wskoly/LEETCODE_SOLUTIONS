import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = Counter(nums)
        frequency_list = list(zip(frequency_dict.values(),frequency_dict.keys()))
        heapq.heapify(frequency_list)
        return [j for i,j in heapq.nlargest(k,frequency_list)]
        