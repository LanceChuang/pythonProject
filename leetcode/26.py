'''Q:Given a sorted array, remove the duplicates in place such that each element appear only once 
and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.'''

arr = []
count = dict()
List = list()
for i in arr:
	count[i] = 1 + count.get(i,0)
	if count[i] > 1:
		count[i] = 1
for k,v in count.items():
	List.append(k)

List.sort()
print(List, len(List))

#不更動原array, 只算重複的部分長度 - O(n)
if not arr: # list沒東西的狀況
	print("0")
newTail = 0 
for i in range(1,len(arr)):
	if arr[i] != arr[newTail]:
		newTail += 1 
		arr[newTail] = arr[i]
print(newTail+1)

