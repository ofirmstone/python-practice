class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {} # using dictionary to store key-value pair (value, location)
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in seenNums:
                return [i, seenNums[pair]]
            
            seenNums[nums[i]] = i