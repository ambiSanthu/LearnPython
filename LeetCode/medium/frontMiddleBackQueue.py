class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue = [val] + self.queue

    def pushMiddle(self, val: int) -> None:
        self.queue.insert((len(self.queue)//2),val)

    def pushBack(self, val: int) -> None:
        self.queue = self.queue + [val]

    def popFront(self) -> int:
        if self.queue == []:
            return -1
        else:
            return self.queue.pop(0)

    def popMiddle(self) -> int:
        if self.queue == []:
            return -1
        else:
            s = len(self.queue)
            if s%2 == 0:
                s=s-1
            return self.queue.pop(s//2)

    def popBack(self) -> int:
        if self.queue == []:
            return -1
        else:
            return self.queue.pop(-1)


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
