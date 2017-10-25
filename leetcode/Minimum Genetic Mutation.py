# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
# Note:

# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.

# Example
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

# return: 2

import collections
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        
        queue = collections.deque()
        queue.append([start,start,0]) # current, previous, steps
        
        while queue:
            current,previous,steps = queue.popleft()
            if current == end:
                return steps
            
            for element in bank: # check which one is next in bank
                if self.findNextOne(current,element) and element != previous:
                    queue.append([element, current, steps+1])
        
        return -1
    
    def findNextOne(self,current,nextMutation):
        change = 0
        for x in xrange(len(current)):
            # check num of different positions
            if current[x] != nextMutation[x]:
                change += 1
        
        return change == 1 
        
        