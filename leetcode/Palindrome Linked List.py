# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?
#Example : madam -> madam 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 為了不使用額外的O(n)空間，我們先用快慢指針找出linked list的中點
# ，找到後從中點之後將linked list反轉再與本來的head前半段比較是否相等，這邊需要一個額外的空間儲存反轉後的linked list。
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        middle = self.findMiddle(head)
        restNode = self.reverseList(middle)
        
        while restNode != None:
            if head.val != restNode.val:
                return False
            head = head.next # move to next for comparing
            restNode = restNode.next
        return True
    
    def findMiddle(self,Node):
        
        fast = Node
        slow = Node
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow # middle point
    
    def reverseList(self,Node):
        # if already meet final node
        if Node == None or Node.next == None:
            return Node
        
        prev = None
        current = Node
        
        while current != None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev # original final node becomes head
    
a = ListNode("m")
b = ListNode("a")
c = ListNode("d")
d = ListNode("a")
e = ListNode("m")
a.next = b
b.next = c
c.next = d
d.next = e 
e.next = None 

solution = Solution()
answer = solution.isPalindrome(a)
print(answer)