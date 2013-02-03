import re, string
class gismu:
	__slots__=['lojbanWord','englishPhrase','xs']


	def __init__(self, lojbanWord,englishPhrase,xs):
	    self.lojbanWord=lojbanWord
	    self.englishPhrase=englishPhrase
	    self.xs=xs
	def __str__(self):
		r=self.lojbanWord+":  "
		for x in range(len(self.xs)):
			r+=("ARG: "+str(x)+" "+self.xs[x])
		return r
def getDict():
	gismuList={}
	later=[]
	engList=[]
	for line in open("wordsEn.txt"):
		engList.append(line.replace("\n",""))
	f=open("gismu.txt")
	for line in f:
		line=line.split()
		#print(line)
		lojbanWord=line[0]
		if(line[1] in engList):
			engWord=line[1]
			i=2
		elif(line[2] in engList):
			engWord=line[2]
			i=3
		elif(line[3] in engList):
			engWord=line[3]
			i=4
		#g=gismu(lojbanWord,engWord,[])
		#print(line)
		rest=line[i:]
		if("x1" in rest):
			if(rest[0][0]!="x"):
				rest=line[i+1:]
			#print(rest)
			s=""

			for z in rest:
				s+=z+" "
			#print(s)
			newS=""
			#s=s.split("x1")
			#s="x1 "+s[len(s)-1]
			for n in range(10,0,-1):
				if(n==1):
					#print(s)
					new=""
					backup=s
					for c in string.punctuation:
						s=s.replace(c," ")
					s=s.replace('/', " ")
					s=s.split()
					#print(s)
					for word in s:
						if word in engList:
							newS+=word+" "
						else:
							break
					rest=newS
					rest=rest.split()
					#print(rest)
					last=rest[len(rest)-1]
					#print(last)
					backup=backup.split()
					#print(backup)
					for word in backup:
						if(last in word):
							#print("end "+word)
							new+=word
							rest=new

							break
						else:
							new+=word+" "
					break
					#print(rest)
				if("x"+str(n) in s):
					#print(s)
					rest=s.split("x"+str(n))
					#print(rest)
					rest=rest[0]+"x"+str(n)
					break

			#At this point we have the word in both languages and "rest"
			#print(rest)

			#print(rest)
			rest=re.split("x\d",rest)
			#print(rest)
			a=[]
			for r in range(len(rest)):
				if r%2==1:
					a.append(rest[r])

			g=gismu(lojbanWord,engWord,a)
			gismuList[lojbanWord]=g
		else:
			later.append(rest)
		#print(later)

	#for x in later:
	#print(gismuList)
	#	print(x)
	return gismuList




def getSentenceFromGismu(lojbanWord,arguments,dictionary):
	curObject=dictionary[lojbanWord]
	retString=""
	try:
		retString+=dictionary[arguments[0]].englishPhrase
	except:
		retString+=arguments[0]
	for x in range(len(arguments)-1):
		retString+=curObject.xs[x]
		try:
			retString+=dictionary[arguments[x+1]].englishPhrase
		except:
			retString+=arguments[x+1]

	return retString

def main():
	print("Loading Dictionary...")
	d=getDict()
	print("Done Loading Dictionary")
	print(getSentenceFromGismu("bridi",["bolci","bruna"],d))
	

main()