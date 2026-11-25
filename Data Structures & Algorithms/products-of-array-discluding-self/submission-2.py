class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for i, j in zip(range(1,len(nums)), range(len(nums)-2, -1, -1)):
            prefix[i] = nums[i-1]*prefix[i-1]
            suffix[j] = nums[j+1]*suffix[j+1]
        
        return [i*j for i, j in zip(prefix, suffix)]