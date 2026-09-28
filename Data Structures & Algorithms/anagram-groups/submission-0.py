class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in cache.keys():
                cache[sorted_word].append(word)
            else:
                cache[sorted_word] = [word]
        
        return list(cache.values())
        