def bruteforce(heights):
    top = max(heights)
    maxAreaFound = 0
    for height in range(1, top+1):
            count = 0
            for i in range(0, len(heights)):
                if heights[i] >= height:
                    count += 1
                else:
                    count = 0
                currentArea = count * height
                maxAreaFound = max(maxAreaFound, currentArea)

    return maxAreaFound


def slightPerformanceIncrease(heights):
    levels = {}
    maxAreaFound = 0
    for height in levels:
            count = 0
            for i in range(0, len(heights)):
                if heights[i] >= height:
                    count += 1
                else:
                    count = 0
                currentArea = count * height
                maxAreaFound = max(maxAreaFound, currentArea)

    return maxAreaFound


def popStack(stack, heights, index, maxArea):

    while stack and stack[-1][1] > heights[index]:
        value = stack.pop()
        length = index - value[0]
        maxArea = max(maxArea, length * value[1])
        start = value[0]
        
    return maxArea, start

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''If you ever read, please don't try the complicated approach with dozens of edge cases, that's not going to get you anywhere.
        try to find a neat strategy or solution'''
        maxArea = 0
        stack = []
        
        start = 0
        for i in range(len(heights)):
            start = i
            # our start marking gets initialized to our current index
            if i != 0 and heights[i-1] > heights[i]:
                maxArea, start = popStack(stack, heights, i, maxArea)
        
            stack.append((start, heights[i]))
        while stack:
            value = stack.pop()
            maxArea = max(maxArea, (len(heights) - value[0]) * value[1])
            
        return maxArea
        
        
        