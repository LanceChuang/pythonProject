
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def get_data(self):   #get data and next in node
		return self.data
	def get_next(self):
		return self.next
	def set_data(self,new_data):     #change the data and next in node
		self.data = new_data
	def set_next(self,new_next):
		self.next = new_next

class UnordererList: 	 	# to refer to the first node
	def __init__(self):
		self.head = None 	#default head links to ground
	def is_empty(self):		#check if the head of the list is a reference to None
		return self.head == None
	def add(self,item):		# add new item to list
		temp = Node(item)	#create a item which resides in a node obj
		temp.set_next(self.head)	#changes the next reference of the new node to refer to the old first node of the list.
		self.head = temp		#attach head to new node

		

mylist = UnordererList()
temp = Node(93)
sure = temp.get_data()
print(sure)
