# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) 
# to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        # 1. Add nums2 to nums1
        index = 0 # index for nums2
        for x in range(m,m+n): # update value from m 
            nums1[x] = nums2[index]
            index += 1
        nums1.sort()    
        # bubble sort
#         for i in range(0,len(nums1)-1):
#             for j in range(0,len(nums1)-1-i):
#                 if nums1[j] > nums1[j+1]:
#                     temp = nums1[j]
#                     nums1[j] = nums1[j+1]
#                     nums1[j+1] = temp


    def merge2(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-2]: # compare last ele in both arrs
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        #condition that nums1 ele > nums2 ele
        if n > 0:
        	print("n = ",n)
        	nums1[:n] = nums2[:n]

# nums1 = [1,5,7,None,None]
# nums2 = [2,3]
# Solution = Solution()
# Solution.merge(nums1,3,nums2,2)
# print(nums1)

nums1 = [50,120,None,None,None,None,None]
nums2 = [3,5,7,8,10]
Solution = Solution()
Solution.merge2(nums1,2,nums2,5)
print(nums1)