import re
class Solution:
    def myAtoi(self, s: str) -> int:
        res = re.match(r'[\s]*([+-]?[0-9]+[0-9]*)',s)
        number = int(res.group(1)) if res else 0
        if number < -2**31:
            return -2**31
        elif number > (2**31)-1:
            return (2**31)-1
        return number 

        