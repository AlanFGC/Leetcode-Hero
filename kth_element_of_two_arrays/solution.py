#User function Template for python3
# my split will be valid if:
# all elements to my left are smaller than all elements to the
# right
def checkCondition(valL1, valL2, valR1, valR2):
    if valL1 <= valR2 and valL2 <= valR1:
        return True
    else:
        return False

class Solution:
    
    
    # think of this as a joint CONDITION where you have a division on one array
    # that depend on a condition of two arrays
    def kthElement(self,  arr1, arr2, n, m, k):
    
        # low can be our pointer to the first array
        
        # high can be our point to the second array
        
        # make sure the second array is correct
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)
        #  we want low to have as few as possible so if k is bigger than m, low will step up
        low = max(0, m-k)
        # we want high to be m-k, but sometimes it might be the case that k is larger than m
        # why n? because WE ARE JUST MANIPULATING THE SMALLEST ARRAY, k is larger
        high = min(k, n)
    
        
        # we need a simple way to define our initial procedure.
        # large array will have k and low array will have 0
        # if large array < k, then low array will help 
        
        # BINARY SEARCH ON THE SMALLEST ARRAY!
        while high > low:
            # do splits for both arrays
            # they will be use for each of our four variable
            splitn = (low + high) // 2
            splitm =  k - splitn
            r1 = r2 = l1 = l2 = 0
            
            #tricky part!
            # we need a conditio than doesn't crash when the the index is larger than the array
            # or index is 0
            if splitn == 0:
                l1 = float('-inf')
            else: l1 = arr1[splitn-1]
            
            if splitm == 0:
                l2 = float('-inf')
            else: l2 = arr2[splitm-1]
            
            
            if splitn == 0:
                r1 = float('inf')
            else: r1 = arr1[splitn]
            
            if splitm == m:
                r2 = float('inf')
            else: r2 = arr2[splitm]
        
            
            if l1 <= r2  and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = splitn - 1
            else:
                low = splitn + 1
        
        return 1
    
   
  # credits this was heavily insipired by:
  # https://www.youtube.com/watch?v=nv7F4PiLUzo&t=1094s
  # I struggled a lot to implement this and it still doesn't work, however I do understand the logic behind it.
