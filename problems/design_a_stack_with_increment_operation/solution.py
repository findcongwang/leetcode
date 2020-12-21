class CustomStack:

    def __init__(self, maxSize: int):
        self.currSize = 0
        self.maxSize = maxSize
        self._stack = [0] * maxSize

    def push(self, x: int) -> None:
        if self.currSize < self.maxSize:
            self._stack[self.currSize] = x
            self.currSize += 1

    def pop(self) -> int:
        if self.currSize <= 0:
            return -1
        else:           
            self.currSize -= 1
            return self._stack[self.currSize]

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.currSize)):
            self._stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)