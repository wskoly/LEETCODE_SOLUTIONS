class Solution:
    def binAdd(self, a,b,c=0):
        a,b,c = int(a), int(b), int(c)
        return (str(a^b^c), (a&b)|(b&c)|(a&c))
    
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        if len(b) > len(a):
            a, b = b,a
        carry = 0
        intermidiate_sum = 0
        high_i = len(a)-1
        low_i = len(b)-1
        while high_i >=0:
            if low_i >= 0:
                intermidiate_sum,carry = self.binAdd(a[high_i], b[low_i], carry)
                result += intermidiate_sum
            else:
                intermidiate_sum,carry = self.binAdd(a[high_i], carry)
                result += intermidiate_sum
            high_i -= 1
            low_i -= 1
        if carry > 0 :
            result += '1'
        
        return result[::-1]
        
        