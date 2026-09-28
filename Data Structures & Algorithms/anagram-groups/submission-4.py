class Solution:
    def get_key_based_on_ascii(self, word):
        # Time Complexity: O(m), Space Complexity: O(1) since arr is a fixed size array
        arr = ['0-'] * 26
        for ch in word:
            index_to_update = ord(ch) - 97
            num_to_update = int(arr[index_to_update].replace('-', ''))
            num_to_update += 1
            arr[index_to_update] = str(num_to_update) + '-'
        return ''.join(arr)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity: O(n * m), Space Complexity: O(n)
        cache = {}
        for word in strs:
            key_for_word = self.get_key_based_on_ascii(word)
            if key_for_word in cache.keys():
                cache[key_for_word].append(word)
            else:
                cache[key_for_word] = [word]
        
        return list(cache.values())
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     # Time Complexity: O(n * m log m), Space Complexity: O(n)
    #     cache = {}
    #     for word in strs:
    #         sorted_word = ''.join(sorted(word))
    #         if sorted_word in cache.keys():
    #             cache[sorted_word].append(word)
    #         else:
    #             cache[sorted_word] = [word]
        
    #     return list(cache.values())
        