# brute force solution
def checkPalindrome(s: string) -> string:
    l = 0
    r = len(s) - 1
    
    while l < r:
        if s[l] != s[r]:
            return None
        l += 1
        r -= 1
        
    return s
        
def bruteForce(self, s: str) -> str:
        maxString = 0
        string = checkPalindrome(s)
        if string:
            return string
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                current = checkPalindrome(s[i:j])
                if current and len(current) > maxString:
                    string = current
                    maxString = len(string)
        
        return string
    
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maxSize = float(-inf)
        sSize = len(s)
        if sSize <= 1:
            return s
        elif sSize == 2 and s[0] != s[1]:
            return s[0]
        
        
        for i in range(sSize):
            l = i
            r = i
            # for odd palindromes
            while l >= 0 and r < sSize:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            r -= 1
            l += 1
            if r - l > maxSize:
                res = s[l:r+1]
                maxSize = len(res)
        
        for i in range(sSize-1):
            if s[i] != s[i+1]:
                continue       
            l = i
            r = i + 1
            while l >= 0 and r < sSize and s[l] == s[r]:   
                l -= 1
                r += 1
    
            l += 1
            r -= 1
            if len(s[l:r+1]) > maxSize:
                res = s[l:r+1]
                maxSize = len(res)
    
        return res
            
            
        
    