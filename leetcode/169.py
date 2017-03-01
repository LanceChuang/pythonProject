'''Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.'''
nums = [1,2,45,654,754,6,5,3,1,2,3,4,5,6,7,7,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
dic = dict()
for i in nums:
	dic[i] = 1 + dic.get(i,0)
# print(dic)
for k,v in dic.items():
	if v > (len(nums)/2):
		maj = k
print(maj)