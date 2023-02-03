# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_nodes = None
        temp = head
        last_duplicate = -101
        if not temp:
            return head
        while temp.next:
            if temp.val != temp.next.val and temp.val != last_duplicate:
                if unique_nodes:
                    unique_nodes.next = temp
                    unique_nodes = unique_nodes.next
                else:
                    head = temp
                    unique_nodes = head
            else:
                last_duplicate = temp.val
            temp = temp.next   
        if temp.val != last_duplicate:
            if unique_nodes:
                unique_nodes.next = temp
                unique_nodes = unique_nodes.next
            else:
                head = temp
                unique_nodes = head
        if not unique_nodes:
            return None
        unique_nodes.next = None

        return head