from collections import OrderedDict


"""
General design.
I am using a hash table to set the keys and values,
then I am using another hash table that has all the frequencies as keys and values as
ordered linked lists.
What's the criteria for eliminating new elements?
1. frequencies, least used will be eleminated first
2. If there is a tie then recently used keys have higher priority to conserve.
"""




class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        
        # main record key:(value, freq)
        self.keys = {} 
        
        # backup record freq:dll
        self.frequencies = OrderedDict()
        
        # Set the first legal frequency, 1.
        self.frequencies[1] = OrderedDict()

        
        
    def get(self, key: int) -> int:
        
        if key not in self.keys:
            return -1
        
        item = self.keys[key]
        
        value = item[0]
        freq = item[1]
        self.updateKey(key, value)
        

        
        return value
        
    
    
    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.updateKey(key, value)
            return
        
        self.size += 1
        
        if self.size > self.cap and self.cap > 0:
            self.popCache()
        elif self.cap == 0:
            return
        
        self.keys[key] = (value, 1)
        
        if 1 not in self.frequencies:
            self.frequencies[1] = OrderedDict()
        
        firstFreqList = self.frequencies[1]
        
        
        
        firstFreqList[key] = (value, 1)
        firstFreqList.move_to_end(key, last=False)
        
     
    
    
    
    # updating my key
    def updateKey(self, key, newValue):
        item = self.keys[key]
        freq = item[1]
        newFreq = freq + 1
        
        self.removeFromDict(freq, key)
        
        if newFreq not in self.frequencies:
            self.frequencies[newFreq] = OrderedDict()
        
        freqList = self.frequencies[newFreq]
        #update the new frequency
        freqList[key] = (newValue, newFreq)
        
        # move to first
        freqList.move_to_end(key, last=False)
        
        # update the main hash
        self.keys[key] = (newValue, newFreq)
        #print(f'{key} should now be in the new freq {newFreq} with a value of {newValue}: {freqList}')
        return

        
    # removes the last item in the whole cache
    def popCache(self):
        
        lowFreq = min( _ for _ in self.frequencies.keys())
        
        # get the last item of the list
        item = self.frequencies[lowFreq].popitem()
        key = item[0]
        
        #print(f'Popping {key} from freq {lowFreq}')
        
        # remove the frequency if empty
        if len(self.frequencies[lowFreq]) == 0:
            del self.frequencies[lowFreq]
        
        # remove item from the main dictionary
        del self.keys[key]
        
        self.size -= 1
        return
        
        

    # removes an item only from the ordered list it is set to
    def removeFromDict(self, freq, key):
        # remove key from frequency list
        del self.frequencies[freq][key]
        
        # if frequency list is empty we remove it.
        if len(self.frequencies[freq]) == 0:
            del self.frequencies[freq]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)