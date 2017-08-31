# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# 思路1:找出長度最小的，然後小的arr假如出現在大的，放在output然後將大的和小的該值去除(=None)
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # dick1,dick2 = {},{}
        output = []
        if len(nums1) > len(nums2):
            big = nums1
            small = nums2
        else:
            big = nums2
            small = nums1
        
        for i in range(len(small)):
            for j in range(len(big)):
                if small[i] == big[j] and small[i]!=None and big[j]!=None:
                    output.append(small[i])
                    big[j] = None
                    small[i] = None
        return sorted(output)

nums1 = [1,2,2,1]
nums2 = [2,2]

Sol = Solution()
answer = Sol.intersect(nums1,nums2)
print(sorted(answer))



# 思路2: 把arr1放入hashtable，然後從arr2去比對值，找到相同後，將arr1在hash table
# 的數-1

class Solution2(object):
	def intersect2(self, nums1, nums2):
		dick , output = {},[]

		for i in nums1:
			dick[i] = dick.get(i,0) + 1

		# 查找element
		for j in nums2:
			if j in dick and dick[j] > 0:
				output.append(j)
				dick[j] -= 1
		return output

nums1 = [2,2]
nums2 = [1,2,2,1]

Sol = Solution2()
answer = Sol.intersect2(nums1,nums2)
print(answer)