class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        
    def push(self, x: int) -> None:
        self.stackA.append(x)
        print(self.stackA)

    def pop(self) -> int:
        if len(self.stackB) > 0:
            return self.stackB.pop(-1)
        
        for i in range(len(self.stackA)):
            self.stackB.append(self.stackA.pop(-1))
        print(self.stackB)
        return self.stackB.pop(-1)

    def peek(self) -> int:
        if len(self.stackB) > 0:
            return self.stackB[-1]
        elif len(self.stackA) > 0:
            for i in range(len(self.stackA)):
                self.stackB.append(self.stackA.pop(-1))
            return self.stackB[-1]
        else:
            return None
        

    def empty(self) -> bool:
        if len(self.stackA) > 0 or len(self.stackB) > 0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()