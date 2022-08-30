# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:          
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = None
        head = None
        def add_data(val):
            nonlocal merged_list
            nonlocal head
            if merged_list == None:
                merged_list = ListNode(val)
                head = merged_list
            else:
                head.next = ListNode(val)
                head = head.next
                
        while list1 != None or list2 != None:
            if list1 == None and list2 != None:
                add_data(list2.val)
                list2 = list2.next
                continue
                
            if list1 != None and list2 == None:
                add_data(list1.val)
                list1 = list1.next
                continue
                
            if list1.val > list2.val:
                add_data(list2.val)
                list2 = list2.next
            elif list1.val == list2.val:
                add_data(list1.val)
                add_data(list2.val)
                list1 = list1.next
                list2 = list2.next
            else:
                add_data(list1.val)
                list1 = list1.next
                
        return merged_list
            
        