class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        #self.items.append(x)
        current_Min = self.getMin()
        if current_Min == None or x < current_Min:
            current_Min = x
        self.items.append((x,current_Min))  # looks like [(1,1),(4,1)]

    def pop(self):
        """
        :rtype: void
        """
        self.items.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.items)== 0:
            return None
        else:
        #return self.items[-1]
            return self.items[-1][0]

    def getMin(self): 
        """
        :rtype: int
        """
        if self.items == []:
            return None
        else:
            return self.items[-1][1]
            
        #return  min(self.items)# need constant time  min() is O(n)
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(155)
obj.push(199)
print(obj.items)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()