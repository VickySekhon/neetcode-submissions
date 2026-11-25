class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict, Counter
        # lookup = defaultdict(int)
        # for i in nums:
        #     lookup[i] += 1
        
        # return list(dict(sorted(lookup.items(), key=lambda x : x[1], reverse=True)).keys())[:k]

        freqs = {}
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        res = [[] for i in range(len(nums)+1)]
        for c, v in freqs.items():
            res[v].append(c)
        
        
        final = []
        for i in range(len(res)-1, -1, -1):
            for num in res[i]:
                print(k, num)
                final.append(num)
                if len(final) == k:
                    return final
        
        return final