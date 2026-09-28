class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [0] * len(nums)
        count = {}
        for num in nums: # O(n)
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1

        for key, val in count.items(): # O(n)
            if freq[val - 1] == 0:
                freq[val - 1] = [key]
            else:
                freq[val - 1].append(key)

        final = []
        i = len(freq) - 1
        while k > 0: # O(1) since k is a constant and cannot be too big
            if freq[i] != 0:
                k = k - len(freq[i])
                for x in freq[i]: # O(n)
                    final.append(x)
                i -= 1
            else:
                i -= 1

        return final
        