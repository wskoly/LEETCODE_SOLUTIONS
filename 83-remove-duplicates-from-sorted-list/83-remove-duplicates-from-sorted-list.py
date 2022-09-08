# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        new_list = ListNode(head.val)
        temp = new_list
        head = head.next
        while head != None:
            if temp.val == head.val:
                head = head.next
                continue
            temp.next = ListNode(head.val)
            temp = temp.next
            head = head.next
            
        return new_list
            