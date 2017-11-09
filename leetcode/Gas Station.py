# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1
        if len(gas) != len(cost) or sum(gas) < sum(cost):
            return -1
        
        position = 0
        balance = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i] # update the balance
            if balance < 0: # balance < 0 means do not go next one => reset the start position
                balance = 0
                position = i + 1
        
        return position

gas = [3,4,3,6,7,1,2]
cost = [2,4,5,1,5,1,3]
Answer = Solution()
ans = Answer.canCompleteCircuit(gas,cost)
print(ans) 