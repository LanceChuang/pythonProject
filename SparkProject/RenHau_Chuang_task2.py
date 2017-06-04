import sys
from operator import add
import math
from pyspark import SparkContext
import time
def weight(arr1,arr2,target):
	arr1 = list(arr1) # active 
	user, movieList = arr1[0], sorted(arr1[1],key=lambda tup:tup[0]) 
	arr2 = sorted(arr2, key=lambda tup: tup[0]) #rest
	i,j = 0,0
	common = list()
	commonP = list()
	rui = None
	while(i<len(movieList) and j<len(arr2)): #find common movie 
		if movieList[i][0] == target:
			rui = movieList[i][1]
		if movieList[i][0] == arr2[j][0]:
			common.append((movieList[i][0],movieList[i][1],arr2[j][1]))
			commonP.append(movieList[i][1])
			i+=1
			j+=1
		elif movieList[i][0] > arr2[j][0]:
			j+=1
		elif movieList[i][0] < arr2[j][0]:
			i+=1
	test , restval,Denominator, Denominator2,Number= 0,0,0,0,0	
	if not common or not commonP or not rui:
		return 0
	for item in common: # avg
		test += item[1]
		restval += item[2]
	average1 = float(test)/float(len(common))  
	average2 = float(restval)/float(len(common))
	for item in common:
		Number += (item[1] - average1)*(item[2]-average2) 
		Denominator += (item[1] - average1)*(item[1] - average1)
		Denominator2 += (item[2]-average2)*(item[2]-average2)

	Denominator = math.sqrt(Denominator)
	Denominator2 = math.sqrt(Denominator2) * Denominator
	if Denominator2 == 0:
		weight = 0
		return (user,weight,commonP,rui) # other's 
	weight = float(Number) / float(Denominator2)
	return (user,weight,commonP,rui)

def Pearson(arr1):
	arr1 = list(arr1) # active 
	user = arr1[0]
	weightValue = arr1[1]
	common = arr1[2]
	rui = arr1[3]
	tot = 0	
	for i in common: # avg ratings
		tot += i
	# print tot
	avg = float(tot) / float(len(common))
	Number = 0	
	return (rui-avg) * weightValue


testingData = "testing_small.csv"
actualData = "ml-latest-small/ratings.csv"
sc=SparkContext(appName="RenHau_Chuang")
rdd1 = sc.textFile(testingData)
rdd2 = sc.textFile(actualData)
header = rdd1.first()
head = rdd2.first()
rdd1 = rdd1.filter(lambda x: x!=header).map(lambda line: line.split(","))\
		.map(lambda x: (x[0],x[1],0.0))\
		.map(lambda h: ( (int(h[0]), int(h[1])), 0.0))
rdd2 = rdd2.filter(lambda x: x!=head).map(lambda line: line.split(","))\
		.map(lambda x: (x[0],x[1],x[2]))\
		.map(lambda h: ( (int(h[0]), int(h[1])),float(h[2])))
samerows = rdd1.join(rdd2).map(lambda x:((x[0][0],x[0][1]),x[1][0]))
training = rdd2.subtractByKey(samerows).map(lambda x: [x[0][0],[(x[0][1],x[1])]])\
			.reduceByKey(lambda a,b: a+b)
# print rdd2.take(5)
f = open('RenHau_Chuang_result_task2.txt', 'w') # write to file 
f.write("UserId,MovieId,Pred_rating\n")
# print rdd1.collect()
res = []
testdata = rdd1.collect()
# testdata = testdata[17202:]
for test in testdata:
	# print test
	testuser = training.filter(lambda x:x[0]==test[0][0]).map(lambda x: x[1])
						# .collect()[0] # test U = training U
	ppap = testuser.collect()[0] # training 
	restuser = training.filter(lambda x:x[0]!=test[0][0]) # test U != training U
	w = restuser.map(lambda x: weight(x,ppap,test[0][1])).filter(lambda x: x!=0)#.collect()

	avgr = sc.parallelize(ppap).map(lambda x: (1,x[1])).reduceByKey(add).collect()[0][1]/len(ppap)
	# print num_pearson
	if not w.collect():
		f.write(str(test[0][0])+','+str(test[0][1])+','+str(avgr)+'\n')
		ans = (test[0], avgr)
		# ans = (test[0],0.5)
	else:
		#tot = w.map(lambda x: (1,x[2])).reduceByKey(add).map(lambda x: x[1]).collect()[0]
		num_pearson = w.map(lambda x: Pearson(x)).filter(lambda x : x!=0)\
							.map(lambda x:(1,x))\
							.reduceByKey(add).collect()

		# print "====numperson==="
		# print num_pearson
		if not num_pearson:
			f.write(str(test[0][0])+','+str(test[0][1])+','+str(avgr)+'\n')
			ans = (test[0], avgr)
			# ans = (test[0], 0.5)
		else:
			rdd3 = w.filter(lambda x : x!=0).map(lambda x: (2,abs(x[1]))).reduceByKey(add)\
			.map(lambda x: x[1]).collect()
	# print rdd3
			# print "========weight==========="
			divide = num_pearson[0][1] / rdd3[0] #out of range
			# print divide
	
	#print "ans: "+str(avgr+divide)
			ans = (test[0], avgr+divide)
			print ans 
			f.write(str(test[0][0])+','+str(test[0][1])+','+str(ans[1])+'\n')
	res.append(ans)


f.close()
rdd5 = sc.parallelize(res)
afterjoin =  rdd5.join(rdd2)
difference = afterjoin.map(lambda x: (abs(x[1][0]-x[1][1])))
print("===after difference===")
zero = difference.filter(lambda x: x>=0.0 and x<1.0).count()
one = difference.filter(lambda x: x>=1.0 and x<2.0).count()
two = difference.filter(lambda x: x>=2.0 and x<3.0).count()
three = difference.filter(lambda x: x>=3.0 and x<4.0).count()
four = difference.filter(lambda x: x>=4.0).count()
print ">=0 and <1: ",zero
print ">=1 and <2: ",one
print ">=2 and <3: ",two
print ">=3 and <4: ",three
print ">=4: ",four
MSE = afterjoin.map(lambda x: (1,math.pow(abs(x[1][0]-x[1][1]),2))).reduceByKey(add).collect()[0][1]/afterjoin.count()
RMSE = math.sqrt(MSE)
print "RMSE = " , RMSE

