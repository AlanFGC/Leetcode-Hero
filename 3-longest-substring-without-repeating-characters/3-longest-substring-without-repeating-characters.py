class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0
        elif size == 1:
            return 1
        
        setOfWords = set()
        windowStart = 0
        windowEnd = 0
        result = 0
        selection = windowEnd
        # KEY IDEA:
        # sliding window works because we have 3 cases:
        # case one selection not in set -> add to set
        # case two selection in set and it's in the very first index -> remove starting element
        # case three selection in set and repetead element not in start -> keep removing till selection is eliminated
        # always keep track of the biggest result.
        while windowEnd < size:
            if s[selection] not in setOfWords:
                setOfWords.add(s[selection])
            elif s[selection] in setOfWords:
                while s[selection] in setOfWords:
                    setOfWords.remove(s[windowStart])
                    windowStart += 1
                setOfWords.add(s[selection])
            windowEnd += 1
            selection = windowEnd
            result = max(result, windowEnd - windowStart)
    
        return result