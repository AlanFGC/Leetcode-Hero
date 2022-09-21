class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        self.sizeA = 0
        self.sizeB = 0
        
    def push(self, x: int) -> None:
        self.stackA.append(x)
        self.sizeA += 1

    def pop(self) -> int:
        if self.sizeB > 0:
            self.sizeB -= 1
            return self.stackB.pop(-1)
        
        for i in range(self.sizeA):
            self.sizeA -= 1
            self.sizeB += 1
            self.stackB.append(self.stackA.pop(-1))

        self.sizeB -= 1
        return self.stackB.pop(-1)

    def peek(self) -> int:
        if self.sizeB > 0:
            return self.stackB[-1]
        elif self.sizeA > 0:
            for i in range(self.sizeA):
                self.sizeA -= 1
                self.sizeB += 1
                self.stackB.append(self.stackA.pop(-1))
            return self.stackB[-1]
        else:
            return None
        

    def empty(self) -> bool:
        if self.sizeA > 0 or self.sizeB > 0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()