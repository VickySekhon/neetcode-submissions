class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort() # log n
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     curr_sum = nums[i] + nums[j]
        #     if curr_sum == target: return [i, j]
        #     if curr_sum > target: j -= 1
        #     else: i += 1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        lookup = {num: index for index, num in enumerate(nums)}
        for i, ele in enumerate(nums):
            need = target - ele
            exists = lookup.get(need)
            if exists and exists != i:
                return [i, lookup[need]]