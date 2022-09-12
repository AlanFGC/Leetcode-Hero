# calculate the median
def calculateMedian(med1, med2):
    print(med1)
    print(med2)
    if med2 == float('-inf') or med2 == float('inf'):
        return med1
    elif med1 == float('-inf') or med1 == float('inf'):
        return med2
    # normal case
    r = float(med1 + med2)
    r = r / 2.0
    return r

def getPosition(m, half):
    RpivS = m
    RpivB = half - RpivS
    return RpivS, RpivB


def offSet(LpivS, RpivS, LpivB, RpivB, arrSmall, arrBig):
    
    # very confusing stuff, just remember that the left one is the 'current previous element' and the right side is 'current next element'
    # we need to check this to move the binary search pivot or index m or middle. if it's on the left or right side. 
    if arrHelp(arrSmall, LpivS) > arrHelp(arrBig, RpivB):
        return -1
    elif arrHelp(arrBig, LpivB) > arrHelp(arrSmall, RpivS):
        return 1
    else:
        return 0

def solution(LpivS, RpivS, LpivB, RpivB, arrSmall, arrBig):
    size = (len(arrSmall) + len(arrBig))
    if (size % 2) == 0:
        # when arr1 + arr2 is even we need to decide which is are the middle elements of all 4 possible ones.
        med1 = max(arrHelp(arrSmall, LpivS), arrHelp(arrBig, LpivB))
        med2 = min(arrHelp(arrSmall, RpivS), arrHelp(arrBig, RpivB))
        return calculateMedian(med1, med2)
    else:
        return min(arrHelp(arrSmall, RpivS), arrHelp(arrBig, RpivB))


def arrHelp(arr, index):
    if index >= len(arr):
        return float('inf')
    elif index < 0:
        return float('-inf')
    return arr[index]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        # we need to differentiate between longer array than smaller array.
        # binary search would be faster on smaller array, especially when length between two arrays is great.
        arrBig = nums1
        arrSmall = nums2
        if len(arrBig) < len(arrSmall):
            arrBig = nums2
            arrSmall = nums1

        RpivS = 1
        RpivB = 1
        half = (len(arrBig) + len(arrSmall)) / 2
        delta = 1
        
        lenB = len(arrBig)
        lenS = len(arrSmall)
        
        # PAINFUL EDGE CASES
        # all are null
        if (lenB + lenS) == 0: 
            return 0
        # one is null
        if lenB == 0:
            if lenS % 2 == 0:
                return calculateMedian(arrSmall[lenS/2 - 1], numS[lenS/2])
            else:
                return arrSmall[lenS/2]
        elif lenS == 0:
            if lenB % 2 == 0:
                print("why are you liek this???")
                return calculateMedian(arrBig[lenB/2 - 1], arrBig[lenB/2])
            else:
                return arrBig[lenB/2]
        # both are length 1
        if lenB == 1 and lenS == 1:
            return calculateMedian(arrSmall[0], arrBig[0])

        #Set index
        l = 0
        r = len(arrSmall)
        # run binary search on the small array, sometimes small array is same size as big arr
        # running binary search this way is better becuase if we make a guess before loop we might face unforseen consequences. 
        while delta != 0:
            middle = (l + r) / 2
            RpivS, RpivB = getPosition(middle, half)
            delta = offSet(RpivS - 1, RpivS, RpivB - 1, RpivB, arrSmall, arrBig)
            if delta < 0:
                r = middle - 1
            elif delta > 0:
                l = middle + 1
        
        return solution(RpivS - 1, RpivS, RpivB - 1, RpivB, arrSmall, arrBig)