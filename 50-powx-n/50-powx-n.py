def helper(x, n, memo):
        if n == 0:
            return 1
        if n == 1:
            return x
        half = n//2

        if (x, n//2) in memo:
            r = memo[(x, half)]
        else:
            r = helper(x, half, memo)
            memo[x, half] = r

        r = r*r
        if n % 2 == 1:
            r = r * x
        return r


class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        result = helper(x, abs(n), memo)
        
        if n < 0:
                result = 1/result
        return result
        
        
        