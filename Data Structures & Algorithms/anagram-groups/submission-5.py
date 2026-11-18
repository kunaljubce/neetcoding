class Solution:
    def str_to_array(self, str):
        return ''.join(sorted(str))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for st in strs:
            st_split = self.str_to_array(st)
            if st_split in cache.keys():
                cache[st_split].append(st)
            else:
                cache[st_split] = [st]
        return list(cache.values())