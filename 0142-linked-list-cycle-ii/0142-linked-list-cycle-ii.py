# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        ptr_dict = {}
        while temp:
            if temp.next in ptr_dict:
                return temp.next
            ptr_dict[temp] = True
            temp = temp.next
        return None