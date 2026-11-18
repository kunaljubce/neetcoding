class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, n in enumerate(nums):
            if n in cache.keys():
                return [min(cache[n], idx), max(cache[n], idx)]
            cache[target - n] = idx
        