# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify
#  the values in the list, only nodes itself can be changed.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1. 先用一個dummy Node當頭, 後面節點移來移去時才不會受影響
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        rest = None # 預備用來儲存後面未處理的節點
        
        while current != None and current.next != None:
            rest = current.next.next # 指向剩餘第一個Node
            current.next.next = current # 第二個node 指向第一個準備做交換
            prev.next = current.next # prev指向第二個node
            
            current.next = rest # 連到剩下的nodes
            
            # 處理下一組
            prev = current
            current = current.next
        
        return dummy.next