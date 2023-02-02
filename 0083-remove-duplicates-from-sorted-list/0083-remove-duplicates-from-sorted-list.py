# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_unique_node = head
        temp = head
        if not temp:
            return head
        while temp.next:
            if temp.val != temp.next.val:
                prev_unique_node.next = temp.next
                prev_unique_node = prev_unique_node.next
            temp = temp.next
        prev_unique_node.next = None

        return head