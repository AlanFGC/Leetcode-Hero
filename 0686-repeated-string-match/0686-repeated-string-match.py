import math
import copy

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        A = copy.copy(a)
        pattern = hash(b) # this will never change
        
            
        # calculate the initial value for a to be >= b
        # original size of A is found in sizeA
        sizeA = len(a)
        sizeB = len(b)
        factor = 1
        
        if sizeA < sizeB:
            factor = math.ceil(len(b)/len(a))
            a = a * factor
            if a == b:
                return factor
        elif sizeA == sizeB and a == b:
            return 1
        elif sizeA > sizeB and b in a:
            return 1
    
        setB = set(b)
        for value in setB:
            if value not in A:
                return -1
        
        # by this point len(a) >= len(b)
        
        while len(a) < (3 * sizeA * factor):
            tail = 0
            i = sizeB
            while i < len(a)+1:
                code = hash(a[tail:i])
                if code == pattern:
                    return len(a)//sizeA
                tail += 1
                i += 1
            # this was the issue
            a += A
        
        return -1
        