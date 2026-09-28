class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            look_for = target - nums[i]
            if look_for in cache.keys():
                return [min(cache[look_for], i), max(cache[look_for], i)]    
            cache[nums[i]] = i

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     # Time complexity: O(n^2), Space complexity: O(1)
    #     res = []
    #     for i in range(0, len(nums)):
    #         look_for = target - nums[i]
    #         for j in range(i+1, len(nums)):
    #             if nums[j] == look_for:
    #                 return [min(i, j), max(i, j)]
            
        