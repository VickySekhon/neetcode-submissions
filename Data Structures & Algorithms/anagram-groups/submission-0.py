class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        mapping = defaultdict(list[str])
        for string in strs:
            mapping["".join(sorted(string))].append(string)
        
        return list(mapping.values())