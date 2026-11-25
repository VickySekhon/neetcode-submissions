class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        # [1,2], [3]
        # 

        nums = [0] * (len(nums1)+len(nums2))
        p, p_1, p_2 = 0, 0, 0
        while p_1 < len(nums1) and p_2 < len(nums2):
            if nums1[p_1] <= nums2[p_2]:
                nums[p] = nums1[p_1]
                p_1 += 1
            elif nums2[p_2] < nums1[p_1]:
                nums[p] = nums2[p_2]
                p_2 += 1
            p += 1
        
        if p_1 < len(nums1):
            while p < len(nums):
                nums[p] = nums1[p_1]
                p+=1
                p_1+=1
        else:
            while p < len(nums):
                nums[p] = nums2[p_2]
                p+=1
                p_2+=1
    

        mid = (len(nums)-1)//2
        if len(nums) % 2 != 0: return nums[mid]
        return (nums[mid] + nums[mid+1])/2