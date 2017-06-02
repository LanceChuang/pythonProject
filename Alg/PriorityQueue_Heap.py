import math
class PriorityQueue(object):
	def __init__(self):
		# self.queue = [None]*10
		self.queue = []
		self.queue.append(0) # default 1st ele so that i can start from 1
		# self.remain = 0
		self.currentLength = 0 # current end point

	def getMax(self):
		return self.queue[1]

	def is_empty():
		return len(self.queue) == 1


	def insert(self,p):
		# if self.currentLength < 9: # default length == 9 
			self.queue.append(p)
			self.currentLength += 1
			self.siftup()

	def siftup(self):
		# find if have parents
		i  = self.currentLength
		 
		while i // 2 > 0: # have parents

			if self.queue[i] > self.queue[i//2]:
				tmp = self.queue[i]
				self.queue[i] = self.queue[i//2]
				self.queue[i//2] = tmp
				i = i // 2 # find if still have parents

			if self.queue[i] < self.queue[i//2]: # child < parent
				break
	
	def remove(self,p):
		for index,ele in enumerate(self.queue):
			if ele == p:
				self.queue[index] = self.queue[-1]
				del self.queue[-1]
				self.currentLength -= 1
				self.siftdown()

	def extractMax(self):
		root = self.queue[1]		
		self.queue[1] = self.queue[-1] # replace root with last node
		del self.queue[-1]
		self.currentLength -= 1
		self.siftdown()
		
		return root

	def siftdown(self):
		# find if root >= child
		i = 1
		while i * 2 <= self.currentLength:
			# confirm to compare with left or right child 
			if i * 2 + 1 <= self.currentLength:
				if self.queue[i*2] > self.queue[i*2+1]:
					tmp = i*2 
				elif self.queue[i*2] <= self.queue[i*2+1]:
					tmp = i*2 + 1
			elif i * 2 + 1 > self.currentLength: # no right child
				tmp = i * 2

			# swap	
			if self.queue[i] < self.queue[tmp]:
				temp = self.queue[tmp]
				self.queue[tmp] = self.queue[i]
				self.queue[i] = temp					
				i = tmp # set i as left child

			elif self.queue[i] >= self.queue[tmp]:
				break

		# maxIndex = 1 # default max 
		# maxElement = self.queue[maxIndex]
		# left_child = self.queue[2 * maxIndex]
		# right_child = self.queue[2 * maxIndex + 1]
		
		# while 2 * maxIndex <= len(self.queue)-1: 
		# 	if maxElement < left_child and maxElement < right_child: 
		# 		if left_child > right_child:
		# 			#swap
		# 			tmp = maxElement
		# 			maxElement = left_child
		# 			left_child = tmp
		# 		elif left_child < right_child:
		# 			#swap
		# 			tmp = maxElement
		# 			maxElement = right_child
		# 			right_child = tmp

		# 	elif maxElement < left_child:
		# 		tmp = maxElement
		# 		maxElement = left_child
		# 		left_child = tmp
		# 	elif maxElement < right_child:
		# 		tmp = maxElement
		# 		maxElement = right_child
		# 		right_child = tmp

		# 		maxIndex += 1

		# 	if 	maxElement > left_child and maxElement > right_child:
		# 		break

answer = PriorityQueue()
answer.insert(1)
answer.insert(2)
answer.insert(3)
answer.insert(19)
answer.insert(88)
answer.insert(5)
print(answer.queue)
# answer.extractMax()
answer.remove(3)
answer.remove(5)
print(answer.queue)
# print(answer.getMax())