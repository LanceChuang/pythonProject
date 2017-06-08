import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from pyspark.sql import DataFrame
from functools import reduce
from pyspark.sql import SQLContext


sc=SparkContext(appName="RenHau_Chuang")
sqlContext = SQLContext(sc)

filename = sys.argv[1]
text = sc.textFile(filename) \
		.map(lambda line: line.split(","))
#     .map(lambda line: ( line[1],float(line[2]) ))
header = text.first()
text = text.filter(lambda h:h!=header).map(lambda h: ( int(h[1]), float(h[2]))) #skip the header 
# print text.take(5) #memory break

count = text.aggregateByKey((0,0), lambda U,v:(U[0]+v, U[1]+1), lambda U1,U2:(U1[0]+U2[0],U1[1]+U2[1]))
# count = text.map(lambda x: (x[0],1))
# print count.take(10)
average = count.map(lambda (x,(y,z)):(x,float(y)/z)).sortByKey()
# print average.take(10)
answer = average.map(lambda ele: list(ele)).collect()
# print answer
for v in answer:
	print v[0],",",v[1]
# movieID = text.map(lambda x: x.split(",")[1])
# print movieID.take(30)
# rating = text.map(lambda x: float(x.split(",")[2])) #change the data type
# print rating.take(30)
# print "FUCKKKKKK"

# print sumRDD.collect()

