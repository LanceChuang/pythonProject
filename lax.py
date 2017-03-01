import sys
import json
f = open("lax.json") #open file and return sucess
lax = json.loads(f.read()) # read the file and return to data var
argu=str(sys.argv[1]) # create a list for arguments input
totY = 0
totT = 0
totIN = 0
tot =0
data = lax["data"]
argu = argu.lower().split()
year = ['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
Terminal = ["t1","t2","t3","t4","t5","t6","tbi"]
INandOUT = ["arrival","departure"]


for i in range(len(data)):
	if data[i][10] == "Terminal 1":
		data[i][10] ="t1"
	elif data[i][10] =="Terminal 2":
		data[i][10] = "t2"
	elif data[i][10] =="Terminal 3":
		data[i][10] = ("t3")
	elif data[i][10] =="Terminal 4":
		data[i][10] = ("t4")
	elif data[i][10] =="Terminal 5":
		data[i][10] = ("t5")
	elif data[i][10] =="Terminal 6":
		data[i][10] = ("t6")
	elif data[i][10] =="Tom Bradley International Terminal":
		data[i][10] = ("tbi")	
	else: continue


# if user input year then return the passengers in that year 
	# if data[i][9][0:4] in argu:
	# 	if data[i][10] not in argu:
	# 		for ran in Terminal:
	# 			argu.append(ran)
	# 	if data[i][11] not in argu:
	# 		for run in INandOUT:
	# 			argu.append(run)
	# 	print (argu)	
	# 	if data[i][10] in argu :
	# 		tot+= int(data[i][13])

# identify 3 situations in year ,terminal , arr/dep
	t1=0
	t2=0
	t3=0
  # check if argu appear in three situations	
	for a in argu:
		if a in year:
			t1=1
		if a in Terminal:
			t2=1
		if a in INandOUT:
			t3=1
	if t1==0:
		argu+=year
	if t2==0:
		argu+=Terminal
	if t3==0:
		argu+=INandOUT

	# print(argu)
	# print(data[i][9])
	# print(data[i][10])
	# print(data[i][11])
	if data[i][9][0:4] in argu and data[i][10] in argu and data[i][11].lower() in argu:
		tot+=int(data[i][13])
		# 	for w in Terminal:
		# 		argu.append(w)
		# 	for u in INandOUT:
		# 		argu.append(u)
		# 	print (argu)	
		# else:
		# 	tot+=int(data[i][13])


			# print ("fuckkkkkkk")
		# print (tot)

	# elif data[i][9][0:4] in argu:
	# elif data[i][9][0:4] in argu :
		# print ("testtttt")
		# tot+= int(data[i][13])
print (tot)	

	# elif data[i][9][0:4] and data[i][10] in argu:
	# 	totT+= int(data[i][13])
	# 	print (argu)	



		#if data[i][10] in argu:
	# for j in year:
		# var1 = str(j)
		# print (type(var1))
		# if var1 in argu:
			# print (var1)

			# for k in Terminal:
			# 	var2 = str(k)
			# 	if var2 in argu:
			# 		# print (var2)
			# 		for l in INandOUT:
			# 			var3 = str(l)
			# 			if var3  in argu:
			# 				# print(var3)
			# 				tot+= int(data[i][13])


# print (tot)
	# for j in year:	
	# 	if data[i][9][0:4] ==j:
	# 		for k in :
	#  			for l in :
	#  				if data[i][10] in :
	#  					tot+= data[i][13]
		# else:
		# 	continue


