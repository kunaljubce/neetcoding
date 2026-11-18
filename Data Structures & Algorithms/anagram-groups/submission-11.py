class Solution:
    def str_to_key(self, str1):
        key = ["0"] * 26
        for char in str1:
            dist_from_a = ord(char) - 97
            key[dist_from_a] = str(int(key[dist_from_a]) + 1)
        # for k in key_arr:
            # key_str += str(k)
        return ','.join(key)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for st in strs:
            st_key = self.str_to_key(st)
            if st_key in cache.keys():
                cache[st_key].append(st)
            else:
                cache[st_key] = [st]
        return list(cache.values())