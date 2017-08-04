# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeElements(self,head,val):

		dummy = pre = ListNode(-1)
		dummy.next = head


		while pre.next:
			if pre.next.val == val:
				pre.next = pre.next.next
			else: # move to next element
				pre = pre.next

		return dummy.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(6)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(6)

a.next = b
b.next = c
c.next = d 
d.next = e 
e.next = f 
f.next = g 
g.next = None

Sol = Solution()
answer = Sol.removeElements(a,6)
print(answer.val)