class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter
        import string

        # mapping = defaultdict(list[str])
        # for string in strs:
        #     mapping["".join(sorted(string))].append(string)
        
        # return list(mapping.values())
        
        # dict_key = {s: 0 for s in string.ascii_lowercase}
        
        # mapping = defaultdict(list[str])

        # for string in strs:
        #     key = dict_key.copy() # O(26) =~ O(1)
        #     for char in string: # O(n)
        #         key[char] += 1
        #     mapping[tuple(key.items())].append(string)
        
        # return list(mapping.values())    
        mapping = defaultdict(list[str])

        for string in strs:
            count = [0] * 26
            for char in string: # O(n)
                count[ord(char) - ord("a")] += 1
            
            mapping[tuple(count)].append(string)
        
        return list(mapping.values())