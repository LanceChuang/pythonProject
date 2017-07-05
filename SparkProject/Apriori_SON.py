import sys
import itertools
import collections
from collections import defaultdict
from collections import Counter
from operator import add
import time
import csv
from pyspark import SparkContext
# start_time = time.time()
caseNum = sys.argv[1]
inputCsv = sys.argv[2]
support = int(sys.argv[3])


# def Compare(arr):
# 	k, v = arr
# 		#print k, v, support
# 	if v >= support:
# 		return k
# 	return

def getCombination(basket, arr, total):
	#basket = list(basket)
	# p_len = basket.count()
	basket = list(basket)		
	p_len = len(basket)
	thres = float(float(float(p_len)/float(total))*float(support))
	out = []
	record = set()
	#print "ppap"
	for i in xrange(len(arr)-1):
		for j in xrange(i+1,len(arr)):
			candidate = set()
			#print arr[i],arr[j]
			for num1, num2 in zip(arr[i],arr[j]):
				candidate.add(num1)
				candidate.add(num2)
			if len(candidate)>len(arr[i])+1:
				continue
			if inputCsv!="ml-20m/ratings.csv":
				if tuple(candidate) in record:
					continue
				record.add(tuple(candidate))
			count = 0
			for line in basket:
				tmp = set(candidate)
				for num in candidate:
					if num in line:
						tmp.remove(num)
				#print candidate, line, tmp
				if not tmp:
					count += 1
			#print candidate, count, thres
			if count>=thres:
				out.append(tuple(sorted(candidate)))
	yield out

def findFrequence(basket, arr, total_x):
	basket = list(basket)
	res = []
	for a in arr:
		a = list(a)
		#print a
		count = 0
		for line in basket:
			#print line
			tmp = set(a)
			for num in a:
				if num in line:
					tmp.remove(num)
			if not tmp:
				count += 1
		res.append((tuple(a),count))
		#print res
	yield res

starttime = time.time()
sc=SparkContext(appName="RenHau_Chuang")

rdd = sc.textFile(inputCsv)
rdd_header = rdd.take(1)[0] #header
# print rdd.getNumPartitions()
rdd1 = rdd.filter(lambda h:h!=rdd_header).map(lambda line: line.split(","))\
				.map(lambda h: ( int(h[0]), int(h[1])))

if caseNum == '1':
	basketcontent = rdd1.map(lambda (x,y): [x,[y]]).reduceByKey(lambda a,b: a+b)\
						.map(lambda x:set(x[1]))#.cache()
else:
	basketcontent = rdd1.map(lambda (x,y): [y,[x]]).reduceByKey(lambda a,b: a+b)\
						.map(lambda x:set(x[1]))#.cache()
rdd1.unpersist()
#basketcontent = userbasket.map(lambda x:set(x[1])).cache() # list

# step 1
frequentItems = basketcontent.flatMap(lambda x: x).map(lambda x: (x,1)).reduceByKey(add)\
					.filter(lambda x: x[1]>=support)
#print frequentItems.collect()
#frequentItems = frequentItems.map(lambda x: Compare(x))
output = frequentItems.map(lambda x: (x[0],))#.distinct()
#print output.collect()
#print result
res = output.map(lambda x: (x[0])).collect() # stuck on this line
print sorted(res)
print "\n"

# step 2
res = output.collect()
#basket = basketcontent.collect()
#b_len = len(basket)
level = 2
while len(res)>1:
	break1 = time.time()
	#print "fuck you"
	#basket = basketcontent.filter(lambda x: len(x)>=level).collect()
	basketcontent = basketcontent.filter(lambda x: len(x)>=level)
	#print "fuck you 2"
	#b_len = len(basket)
	b_len = basketcontent.count()
	#print "test@"
	comb = basketcontent.mapPartitions(lambda b: getCombination(b, res, b_len))\
			.flatMap(lambda x: x).distinct().collect()
	#print comb#.collect()
	#comb = comb.flatMap(lambda x: x).reduceByKey(add).map(lambda x: x[0])
	# print "comb time: " + str(time.time()-break1)
	break2 = time.time()
	total_x = len(comb)
	if not total_x:
		break
	#print "lance"
	#basket = basketcontent.collect()
	res = basketcontent.mapPartitions(lambda x: findFrequence(x, comb, total_x))\
				.flatMap(lambda x: x).reduceByKey(add).filter(lambda x: x[1]>=support)\
				.map(lambda x: x[0]).collect()
	#print len(res)
	#res = output.collect()	
	print sorted(res)
	# print "out time: " + str(time.time()-break2)
	print "\n"
	level += 1
# print time.time()-starttime