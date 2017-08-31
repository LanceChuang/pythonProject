class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.instack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.outstack == [] and self.instack == [] # # check both stacks considering no popping situation



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
# param_2 = obj.pop()
# print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)