# go through every iteration, use a set to keep track of numbers
# current element is an int, and use n-1 power - index to calculate value
# added to current
# time complexity is n! + sorting + generating everything
def bruteforceSol(index, maxIndex, options, current, currentOptions: set, res):
    if index >= maxIndex:
        res.append(current)
        return
    n = maxIndex
    for i in range(len(options)):
        if options[i] not in currentOptions:
            current += options[i] * math.pow(10, (n - 1)  - index)
            currentOptions.add(options[i])
            bruteforceSol(index + 1, maxIndex, options, current, currentOptions, res)
            current -= options[i] * math.pow(10, (n - 1) - index)
            currentOptions.remove(options[i])
            


def recursiveSmart(n, k, options):
    if n == 0:
        return ""
    res = "" 
    # all number that currently available
    x = math.factorial(n)
    # size of our chunks
    size = x // n
    
    res += str(options[k // size])
    
    
    # how to generate next chunk
    # we use mod to calculate the next iteration's k
    # so size is size of our chunk, we want to know where does k fall
    # if we were to calcualte where would it fall inside that new size
    newK = k % size 
    # options will track all available options, in this case,
    # we can remove it from the array because we risk choosing the kth element
    # once again
    options.pop(k // size)
    return res + recursiveSmart(n-1, newK, options)
    
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        options = []
        res = ""
        for i in range(n):
            options.append(i+1)
        
        return recursiveSmart(n, k-1, options)
        
        
    
    
    # generate all possible permutations, backtracking recursively
    def bruteForce(n, k):
        x = math.factorial(n)
        print("My n has", x, " elements, we want the ", k ,"th number in the sequence.")
        # recursive way!
        options = []
        for i in range(n):
            options.append(i+1)
        current = 0
        res = []
        currentOptions = set()
        bruteforceSol(0, n, options, current, currentOptions, res)
        # sort and get the final value. 
        res.sort()
        return str(int(res[k-1]))