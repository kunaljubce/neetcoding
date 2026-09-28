class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if n in count.keys():
                count[n] += 1
            else:
                count[n] = 1
        
        for _, value in count.items():
            if value > 1:
                return True

        return False
    # Run time O(n) = nlog(n) + n, space complexity = O(1)
    # The nlog(n) is attributed to the sort and then a single pass through is O(n)
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     if len(nums) <= 1:
    #         return False

    #     nums.sort()
    #     for i in range(len(nums)):
    #         if i < len(nums) - 1 and nums[i] == nums[i + 1]:
    #             return True

    #     return False

    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     # Run time O(n) = n^2, space complexity = O(1)
    #     if len(nums) <= 1:
    #         return False

    #     for i in range(0, len(nums)): 
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums [j]:
    #                 return True

    #     return False

        