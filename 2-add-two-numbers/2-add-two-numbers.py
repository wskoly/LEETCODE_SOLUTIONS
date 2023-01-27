class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_l1 = l1
        temp_l2 = l2
        result = None
        temp_result = None
        carry = 0
        while temp_l1 != None or temp_l2 != None:
            a,b = 0,0
            if temp_l1 != None:
                a = temp_l1.val
                temp_l1 = temp_l1.next
            if temp_l2 != None:
                b = temp_l2.val
                temp_l2 = temp_l2.next
            _sum = (a+b+carry)%10
            carry = (a+b+carry)//10
            _node = ListNode(_sum)
            if result == None:
                result = _node
                temp_result = result
                continue
            temp_result.next = _node
            temp_result = temp_result.next
        if carry > 0:
            temp_result.next = ListNode(carry)
        return result
