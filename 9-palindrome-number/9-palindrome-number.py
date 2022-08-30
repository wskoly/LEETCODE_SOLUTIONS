class Solution(object):
    def isPalindrome(self, x):
        """
        Without coverting string
        """
        if x<0:
            return False
        digit_count = 0
        digits = []
        temp = x
        while temp>0:
            digit_count +=1
            digits.append(temp%10)
            temp //=10
        reverse_num = 0
        i = len(digits)-1
        for digit in digits:
            reverse_num += digit *(10**i)
            i -=1 
        return (reverse_num == x)