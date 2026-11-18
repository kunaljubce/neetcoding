class Solution:
    def str_to_array(self, str):
        return ''.join(sorted(str))

    def str_to_key(self, str):
        key = ["0"] * 26
        for char in str:
            dist_from_a = ord(char) - 97
            key[dist_from_a] = "1"
        return ''.join(key)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for st in strs:
            st_key = self.str_to_array(st)
            if st_key in cache.keys():
                cache[st_key].append(st)
            else:
                cache[st_key] = [st]
        return list(cache.values())