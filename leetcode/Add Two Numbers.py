# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		dummy = pre = ListNode(0)
		rest = 0 # 處理溢位

		#當 list1, list2 都沒有值，而且rest也為0的時候才結束迴圈
		while l1 != None or l2 != None or rest > 0:
			value = 0

			# list1與list2長度可能不同，分開處理
			if l1 != None:
				value += l1.val
				l1 = l1.next
			if l2 != None:
				value += l2.val
				l2 = l2.next

			#如果之前有進位，rest = 1；沒有的話rest = 0
			value += rest 
			#相加如果超過9，只能留下個位數放入結果list，十位數的地方進位
			pre.next = ListNode(value%10)
			rest = value // 10

			pre = pre.next
		
		return dummy.next

a = ListNode(2)
b = ListNode(4)
c = ListNode(9)
a.next = b
b.next = c
c.next = None 

e = ListNode(5)
f = ListNode(6)
g = ListNode(9)
e.next = f 
f.next = g 
g.next = None
answer = Solution()
ans = answer.addTwoNumbers(a,e)
print(ans.val)
print(ans.next.val)
print(ans.next.next.val)
print(ans.next.next.next.val)
