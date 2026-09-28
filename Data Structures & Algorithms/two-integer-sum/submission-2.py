class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            # if target > 0 and nums[i] <= target:
            look_for = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == look_for:
                    return [min(i, j), max(i, j)]
            
        