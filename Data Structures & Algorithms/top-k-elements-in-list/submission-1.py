class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}
        for i in nums:
            if frequencies.get(i) is None:
                frequencies[i] = 1
            else:
                frequencies[i] += 1
        
        return list(dict(sorted(frequencies.items(), key=lambda x : x[1], reverse=True)[:k]).keys())