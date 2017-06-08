'''
calculate the average rating of each tag.
Both ratings.csv and tags.csv

'''


import sys
import time
import csv
from pyspark import SparkConf, SparkContext

# start_time = time.time()

sc=SparkContext(appName="RenHau_Chuang")
filename1 = sys.argv[1]
filename2 = sys.argv[2]
outputpath = sys.argv[3]

text = sc.textFile(filename1) 
text2 = sc.textFile(filename2) 
rawdata_header = text.take(1)[0]
rawdata_header2 = text2.take(1)[0]

ratings = text.filter(lambda h:h!=rawdata_header).map(lambda line: line.split(",")).map(lambda h: ( int(h[1]), float(h[2]))).cache() #skip the header 
# print ratings.take(5) 
tags = text2.filter(lambda h:h!=rawdata_header2).map(lambda line: line.split(",")).map(lambda h: (int(h[1]), h[2])).cache() # convert tag to str

count = ratings.aggregateByKey((0,0), lambda U,v:(U[0]+v, U[1]+1), lambda U1,U2:(U1[0]+U2[0],U1[1]+U2[1]))
# print count
average = count.map(lambda (x,(y,z)):(x,float(y)/z))#.sortByKey(False)
# print average.take(5)

# full_movie = tags.join(average).map(lambda x : x[1]).sortByKey(False)#.distinct()#.map(lambda o:[o[0][1],o[1][1]]).sortByKey()
full_movie = average.join(tags).map(lambda x : x[1]).map(lambda o: (o[1].encode("utf-8"), o[0])).sortByKey(False)#.distinct()#.map(lambda o:[o[0][1],o[1][1]]).sortByKey()
# print full_movie.take(5)

answer = full_movie.aggregateByKey((0,0), lambda U,v:(U[0]+v, U[1]+1), lambda U1,U2:(U1[0]+U2[0],U1[1]+U2[1]))
#collect()
average = answer.map(lambda (x,(y,z)):(x,float(y)/z)).sortByKey(False)
answer = average.collect()

# header = ['tag','rating_avg']
header = ["tag","rating_avg"]
f =	open(outputpath,'w')
w = csv.writer(f)
w.writerow(header)
for i in answer:
	record = [i[0],str(i[1])]
	w.writerow(record)
f.close()	
# print "tag, rating_avg"
# for i in answer:
	# print i[0], i[1]


# answer = average.collect()

# tags_for_join = tags.sortByKey(False)	
# print tags_for_join.take(5)
# full_movie = average.join(tags_for_join).map(lambda x: (x[1][1],x[1][0]))
# print full_movie.take(5)
# rating_title = header.split(",")[2].encode("utf-8")
# tag_title = header2.split(",")[2].encode("utf-8")
# print rating_title, ",", tag_title
# for v in answer:
	# if type(v[1]) is str:
		# v[1]=v[1].encode("utf-8")
	# print v[0].encode("utf-8"),",",v[1]

# print time.time() - start_time
