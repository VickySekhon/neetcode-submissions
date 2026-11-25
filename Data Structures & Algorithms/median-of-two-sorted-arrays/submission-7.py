import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        # # [1,2], [3]
        # # 

        # nums = [0] * (len(nums1)+len(nums2))
        # p, p_1, p_2 = 0, 0, 0
        # while p_1 < len(nums1) and p_2 < len(nums2):
        #     if nums1[p_1] <= nums2[p_2]:
        #         nums[p] = nums1[p_1]
        #         p_1 += 1
        #     elif nums2[p_2] < nums1[p_1]:
        #         nums[p] = nums2[p_2]
        #         p_2 += 1
        #     p += 1
        
        # if p_1 < len(nums1):
        #     while p < len(nums):
        #         nums[p] = nums1[p_1]
        #         p+=1
        #         p_1+=1
        # else:
        #     while p < len(nums):
        #         nums[p] = nums2[p_2]
        #         p+=1
        #         p_2+=1
    

        # mid = (len(nums)-1)//2
        # if len(nums) % 2 != 0: return nums[mid]
        # return (nums[mid] + nums[mid+1])/2
        # if len(nums1) == 0: return nums2[(len(nums2)-1)//2] if len(nums2)%2!=0 else (nums2[(len(nums2)-1)//2] + nums2[(len(nums2))//2])/2
        # elif len(nums2) == 0: return nums1[(len(nums1)-1)//2] if len(nums1)%2!=0 else (nums1[(len(nums1)-1)//2] + nums1[(len(nums1))//2])/2

        l, r = 0, len(min(nums1, nums2, key=len))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        half = (len(nums1)+len(nums2))//2
        while l <= r:
          # partitions
          i = (l+r)//2
          j = half-i
          
          # Nothing on the left side
          if i <= 0:
            a_left_max = -float('inf')
          else:
            a_left_max = nums1[i-1]
          
          if j <= 0:
            b_left_max = -float('inf')
          else:
            b_left_max = nums2[j-1]
          
          # Nothing on the right side  
          if i == len(nums1):
            a_right_min = float('inf')
          else:
            a_right_min = nums1[i]
          
          if j == len(nums2):
            b_right_min = float('inf')
          else:
            b_right_min = nums2[j]
            
          print(i)
          
          print(f"a = [...{a_left_max}|{a_right_min}...]")
          print(f"b = [...{b_left_max}|{b_right_min}...]")
          
          if a_left_max <= b_right_min and b_left_max <= a_right_min:
            if (len(nums1) + len(nums2)) % 2 == 0: # even length, median is the average of the 
              median = (max(b_left_max, a_left_max) + min(b_right_min, a_right_min))/2
            else: # odd length, median is the middle element
              #median = max(b_left_max, a_left_max)
              median = min(b_right_min, a_right_min)
            return median
          else:
            if b_left_max > a_right_min:
              l = i+1
            else:
              r = i-1