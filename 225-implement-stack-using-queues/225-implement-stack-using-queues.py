class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        
        
    def pop(self) -> int:
        for i in range(len(self.queue)-1):
            self.push(self.queue.pop(0))
        return self.queue.pop(0)

    def top(self) -> int:
        for i in range(len(self.queue)):
            if i == len(self.queue)-1:
                res = self.queue.pop(0)
                self.push(res)
            else:
                self.push(self.queue.pop(0))
        return res

    def empty(self) -> bool:
        if len(self.queue) > 0:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()