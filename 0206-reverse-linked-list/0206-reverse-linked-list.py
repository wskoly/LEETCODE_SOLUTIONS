# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = None
        temp = head
        while temp:
            node = ListNode(temp.val)
            node.next = reversed_list
            reversed_list = node
            temp = temp.next
        return reversed_list