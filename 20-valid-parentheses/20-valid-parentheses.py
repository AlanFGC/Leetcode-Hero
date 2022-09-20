class Solution:
    def isValid(self, s: str) -> bool:
        openChars = {'(', '{', '['}
        closeChars = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in range(len(s)):
            
            if s[i] in openChars:
                # puts this in the first position
                stack.append(s[i])
            elif len(stack) == 0 or closeChars[s[i]] != stack[-1]:
                return False
            else:
                # pops the last time
                stack.pop()
        
        if len(stack) != 0:
            return False
        
        return True