class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        lookup = defaultdict(int)
        for i in nums:
            lookup[i] += 1
        
        return list(dict(sorted(lookup.items(), key=lambda x : x[1], reverse=True)).keys())[:k]