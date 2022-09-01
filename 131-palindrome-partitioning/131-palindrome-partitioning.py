def isPalindrome(word, dp):
    if word in dp:
        return dp[word]
    
    size = len(word)
    if size <= 1:
        return True
    index = 0
    index2 = size - 1
    while index < index2:
        if word[index] != word[index2]:
            dp[word] = False
            return False
        index += 1
        index2 -= 1
    dp[word] = True
    return True

def backtrack(index, currComb, length, res, s, dp):
    if index != 0 and not isPalindrome(currComb[-1], dp):
        return
    elif index >= length:
        res.append(currComb.copy())

    for i in range(index + 1 , length + 1):
        # append inserts to the end
        currComb.append(s[index:i])
        backtrack(i, currComb, length, res, s, dp)
        currComb.pop()
    
        


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #brute force approach try all possible partions
        # from n -1  partitions to 0 partitions
        # Don't reframe problem as dp just yet, REMEBER when it comes to combinations
        # and sets, usually is backtracking
        res = []
        length = len(s)
        currentComb = []
        index = 0
        dp = {"":True}
        backtrack(index, currentComb, length, res, s, dp)
        return res