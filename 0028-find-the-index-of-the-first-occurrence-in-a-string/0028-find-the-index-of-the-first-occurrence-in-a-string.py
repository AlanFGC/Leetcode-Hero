class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        code = hash(needle)
        
        
        if len(needle) == 1:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    return i
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                currCode = hash(haystack[i:i+len(needle)])
                if code == currCode:
                    return i
        
        hayCode = hash(haystack)
        
        if hayCode == code:
            return 0
        
        return -1
        