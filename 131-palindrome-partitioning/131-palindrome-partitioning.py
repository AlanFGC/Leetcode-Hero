def isPalindrome(word):
    size = len(word)
    if size <= 1:
        return True
    index = 0
    index2 = size - 1
    while index < index2:
        if word[index] != word[index2]:
            return False
        index += 1
        index2 -= 1
    return True

def backtrack(index, currComb, length, res, s):
    if index != 0 and not isPalindrome(currComb[-1]):
        return
    elif index >= length:
        res.append(currComb.copy())

    for i in range(index + 1 , length + 1):
        # append inserts to the end
        currComb.append(s[index:i])
        backtrack(i, currComb, length, res, s)
        currComb.pop()
    
        


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #brute force approach try all possible partions
        # from n -1  partitions to 0 partitions
        # Don't reframe problem as dp, REMEBER when it comes to combinations
        # and sets, usually is backtracking
        res = []
        length = len(s)
        currentComb = []
        index = 0
        backtrack(index, currentComb, length, res, s)
        return res