class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # for char in s:
        #     if char not in t:
        #         return False
        #     t = t.replace(char, '', 1)

        # return len(t) == 0

        counts = {}
        for ch_s, ch_t in zip(s, t):
            counts[ch_s] = counts.get(ch_s, 0) + 1
            counts[ch_t] = counts.get(ch_t, 0) - 1

        return all(val == 0 for val in counts.values())

        