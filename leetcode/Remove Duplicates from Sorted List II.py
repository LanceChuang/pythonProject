# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution(object):
	def deleteDuplicates(self,head):
		if not head:
			return 
		'''dummy = cur 指到同個地方,所以cur.next = l1 -> dummy.next = l1'''
		dummy = pre = ListNode(0) # 之後任何變動只會變動pre , dummy維持0
		dummy.next = head
		# print("dummy.next is {}".format(dummy.next.val))
		# print("pre.next is {}".format(pre.next.val))
		# pre.next = ListNode(12345)
		# print("dummy.next is {}".format(dummy.next.val))
		# print("pre.next is {}".format(pre.next.val))
		while head and head.next:
			if head.val == head.next.val:
				while head.next and head.val == head.next.val:
					head = head.next
				head = head.next
				pre.next = head
				# print("dummy.next is {}".format(dummy.next.val))
				# print("pre.next is {}".format(pre.next.val))
			else:
				pre = pre.next # move to next ele as dummy
				# print("pre is ",pre.val)
				# print("dummy is ",dummy.val)
				head = head.next
		# print("dummy is ",dummy.val)

		return dummy.next



a = ListNode(1)
b =ListNode(1)
c =ListNode(1)
d =ListNode(2)
e =ListNode(3)
f =ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f 
f.next = None
answer = Solution()
ans = answer.deleteDuplicates(a)
print(ans.val)


