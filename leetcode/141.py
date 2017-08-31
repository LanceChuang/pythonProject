# Linked List Cycle
# Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        marker1 = head
        marker2 = head
        
        while marker2 != None and marker2.next != None:
            
            marker1 = marker1.next
            marker2 = marker2.next.next
            if marker1 == marker2:
                return True
                
        return False

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = a

Sol = Solution()
ans = Sol.hasCycle(a)
print(ans)

