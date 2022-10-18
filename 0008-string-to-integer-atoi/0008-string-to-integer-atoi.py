nums = {'1','2','3','4','5','6','7','8','9','0'}

class Solution:
    def myAtoi(self, s: str) -> int:
        # strip whitespace
        s = s.strip()
        
        if len(s) == 0:
            return 0
        # get a minus flag to tell if the our final value is negative
        minus = False
        
        # check for symbols and remove them.
        if s[0] == '-' :
            s = s[1:]
            minus = True
        elif s[0] == '+':
            s = s[1:]
        
        
        
        arr = []
        for i in range(len(s)):
            if s[i] not in nums:
                break
            arr.append(s[i])
        # print(arr)
        base = 1
        
        value = 0
        
        for i in range(len(arr)-1, -1, -1):
            value += int(arr[i]) * base
            base *= 10
    
        if minus:
            value *= -1
        if value < -2147483648:
            return -2147483648
        elif value > 2147483647:
            return 2147483647
        
        return value
            