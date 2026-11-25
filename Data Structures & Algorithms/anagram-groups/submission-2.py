class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter
        import string

        # mapping = defaultdict(list[str])
        # for string in strs:
        #     mapping["".join(sorted(string))].append(string)
        
        # return list(mapping.values())
        
        dict_key = {s: 0 for s in string.ascii_lowercase}
        
        mapping = defaultdict(list[str])

        for string in strs:
            key = dict_key.copy()
            for char in string:
                key[char] += 1
            mapping[tuple(key.items())].append(string)
        
        return list(mapping.values())