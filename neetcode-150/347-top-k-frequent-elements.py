from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums 
        
        freq = Counter(nums)

        return [num for num, count in freq.most_common(k)]
