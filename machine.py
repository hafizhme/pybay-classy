from sys import argv

class Machine:
	def __init__(self):
		pass

		self.frequency = {
			1 : [0,0,0,0],
			2 : [0,0,0,0],
			3 : [0,0,0,0],
			4 : [0,0,0,0],
			5 : [0,0,0,0],
			6 : [0,0,0,0],
			7 : [0,0,0,0],
			8 : [0,0,0,0],
			9 : [0,0,0,0],
			10: [0,0,0,0],
		}
		self.quartile = {
			1 : [0,0,0],
			2 : [0,0,0],
			3 : [0,0,0],
			4 : [0,0,0],
			5 : [0,0,0],
			6 : [0,0,0],
			7 : [0,0,0],
			8 : [0,0,0],
			9 : [0,0,0],
			10: [0,0,0]
		}
		self.data = []

		self.upbot = {
			1 : [0,0],
			2 : [0,0],
			3 : [0,0],
			4 : [0,0],
			5 : [0,0],
			6 : [0,0],
			7 : [0,0],
			8 : [0,0],
			9 : [0,0],
			10: [0,0],
		}

	def readdt(self, filedir):
		f = open(filedir, "r")
		f.readline()
		a = f.readline()
		while (a is not ""):
			self.data.append([ float(x) for x in a.replace("\n","").split(',')])
			a = f.readline()

		self.upbot = {
			1 : [self.data[0][1],self.data[0][1]],
			2 : [self.data[0][2],self.data[0][2]],
			3 : [self.data[0][3],self.data[0][3]],
			4 : [self.data[0][4],self.data[0][4]],
			5 : [self.data[0][5],self.data[0][5]],
			6 : [self.data[0][6],self.data[0][6]],
			7 : [self.data[0][7],self.data[0][7]],
			8 : [self.data[0][8],self.data[0][8]],
			9 : [self.data[0][9],self.data[0][9]],
			10 : [self.data[0][10],self.data[0][10]],
		}

	# def sepx(self):
	# 	for i in range(1,11):
	# 		self.x[i].append(self.data[0][i])
	# 		for j in range(1,len(self.data)):
	# 			k = 0
	# 			cont = (self.data[j][i] < self.x[i][k])
	# 			while cont:
	# 				print("i :",i,"j : ",j,"k :",k)
	# 				if k < j-1:
	# 					k = k + 1
	# 					cont = (self.data[j][i] < self.x[i][k])
	# 				else:
	# 					cont = False
	# 			self.x[i].insert(k,self.data[j][i])


	def bounding(self):
		for line in self.data:
			for i in range(1,11):
				if (self.upbot[i][0] > line[i]):
					self.upbot[i][0] = line[i]
				if (self.upbot[i][1] < line[i]):
					self.upbot[i][1] = line[i]
		for i in range(1,11):
			self.quartile[i][0] = (self.upbot[i][1] - self.upbot[i][0]) * 0.25
			self.quartile[i][1] = (self.upbot[i][1] - self.upbot[i][0]) * 0.5
			self.quartile[i][2] = (self.upbot[i][1] - self.upbot[i][0]) * 0.75
			print(self.quartile[i])


	def frequencying(self):
		for line in self.data:
			for i in range(1,11):
				if line[i] < self.quartile[i][0]:
					self.frequency[i][0] += 1
				elif line[i] < self.quartile[i][1]:
					self.frequency[i][1] += 1
				elif line[i] < self.quartile[i][2]:
					self.frequency[i][2] += 1
				else:
					self.frequency[i][3] += 1

		for i in range(1,11):
			print(self.frequency[i])
