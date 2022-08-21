def helper(x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        
        r = helper(x, n//2)
        print(r)
        r = r*r
        if n % 2 == 1:
            r = r * x
        return r


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = helper(x, abs(n))
        
        if n < 0:
                result = 1/result
        return result
        
        
        