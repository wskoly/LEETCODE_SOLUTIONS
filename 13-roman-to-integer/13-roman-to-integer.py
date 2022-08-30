class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        double_symbol = {'IV':4, 'IX':9,'XL':40, 'XC':90, 'CD':400, 'CM':900}
        
        num = 0
        
        for key in double_symbol:
            num += s.count(key)*double_symbol[key]
            s = s.replace(key,'')
            
        for key in symbol_val:
            num += s.count(key)*symbol_val[key]
            
        return num