# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3

'''If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        diff = self.findDifference(headA,headB)
        
        # find intersection node
        if diff > 0: # headA's length longer
            while diff > 0:
                headA = headA.next # move head until diff == 0 (length == headB)
                diff -= 1
        else: # headB's length longer
            while diff < 0:
                headB = headB.next
                diff += 1
        
        # compare node 
        while headA:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
    
    def findDifference(self,headA,headB):
        A_length = 0
        B_length = 0
        
        while headA:
            A_length += 1
            headA = headA.next
        
        while headB:
            B_length += 1
            headB = headB.next
        
        return A_length - B_length # difference