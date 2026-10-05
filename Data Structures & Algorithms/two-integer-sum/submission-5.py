class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, x in enumerate(nums):
            find = target - x
            if find not in result.keys():
                result[x] = i
            else:
                return [min(i, result[find]), max(i, result[find])]

        