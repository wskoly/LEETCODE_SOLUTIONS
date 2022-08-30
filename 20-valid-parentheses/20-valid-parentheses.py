class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_associate = {')':'(',  '}':'{', ']':'['}
        paren_stack = []
        is_valid = True
        for paren in s:
            if paren in paren_associate:
                try:
                    if not paren_associate[paren] == paren_stack.pop():
                        is_valid = False
                        break
                    else:
                        continue
                except:
                    is_valid = False
                    break
                    
            paren_stack.append(paren)
                    
        return (not bool(len(paren_stack))) and is_valid