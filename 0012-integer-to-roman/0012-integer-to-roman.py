class Solution:
    def intToRoman(self, num: int) -> str:
        r_map = {1000:'M',900:'CM',500:'D', 400:'CD',
                 100:'C',90:'XC',50:'L',40:'XL',
                 10:'X',9:'IX',5:'V',4:'IV',3:'III',2:'II', 1:'I'}
        roman = ''
        for i in r_map:
            roman += r_map[i]*(num//i)
            num %= i
        return roman