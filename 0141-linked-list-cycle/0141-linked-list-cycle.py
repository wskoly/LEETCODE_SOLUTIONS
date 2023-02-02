# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        ptr_list = []
        while temp:
            if id(temp.next) in ptr_list:
                return True
            ptr_list.append(id(temp))
            temp = temp.next
        return False