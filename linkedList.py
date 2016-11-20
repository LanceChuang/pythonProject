
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
	def size(self):			#count the number of nodes
		current = self.head
		count = 0
		while current != None:				#as long as current reference is not None, move current to the next node
			count += 1
			current = current.get_next()

		return count 
	
	def search(self,item):
		current = self.head
		found = False  				#boolean var to remember if have located the item we are searching for
		while  current !=None and not found:
			if current.get_data()==item:
				found = True
			else:
				current = current.get_next()
		
		return	found		#return the result that whether we found the item we are searching for	
		

mylist = UnordererList()
temp = Node(93)
sure = temp.get_data()
mylist.add(8)
mylist.add(12)
print(mylist.search(8))
size = mylist.size()
print(size)
