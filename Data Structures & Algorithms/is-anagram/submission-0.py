class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in s:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1

        for j in t:
            if j not in count.keys():
                # found a char in t not present in s, so not an anagram
                return False
            else:
                count[j] -= 1

        for k in count.values():
            if k != 0:
                # If k < 0, means t had more repetitions of a char than s
                # If k > 0, means t had less repetitions of a char than s
                return False
        
        return True