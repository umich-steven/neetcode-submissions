class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            key = [0] * 26
            for i in word:
                list(key)
                key[ord(i) - ord('a')] += 1
            key = tuple(key)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(word)
            
        return list(hash_map.values())     
            
            