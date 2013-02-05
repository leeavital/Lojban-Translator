import re, string
class gismu:
	__slots__=['lojbanWord','englishPhrase','xs']


	def __init__(self, lojbanWord,englishPhrase,xs):
	    self.lojbanWord=lojbanWord
	    self.englishPhrase=englishPhrase
	    self.xs=xs
	def __str__(self):
		r=self.lojbanWord+":  "
		z=0
		for x in range(len(self.xs)):
			r+=("ARG: "+str(x)+" "+self.xs[x])
			z=x
		return r+"ARG: "+str(z+1)
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
			a=rest[1:-1]
			#for r in range(len(rest)):
			#	if r%2==1:
			#		a.append(rest[r])
			#print(a)
			g=gismu(lojbanWord,engWord,a)
			gismuList[lojbanWord]=g
		else:
			later.append(rest)
		#print(later)

	#for x in later:
	#print(gismuList)
	#	print(x)
	return gismuList

def getCmavo():
	f=open("cmavo.txt")
	d={}
	for line in f:

		newLine=re.split(r"\W{10}",line)
		newLine=newLine[0].split()
		t=newLine[2:]
		trans=""
		for x in t:
			trans+=x+" "

		d[newLine[0]]=trans

	return d

def getSentenceFromGismu(lojbanWord,arguments,dictionary,dictionary2):
	curObject=dictionary[lojbanWord]
	print(curObject.xs)

	retString=""

	for x in range(len(arguments)):
		if(arguments[x] in dictionary):
			retString+=dictionary[arguments[x]].englishPhrase
		elif(arguments[x] in dictionary2):
			retString+=dictionary2[arguments[x]]
		else:
			retString+=arguments[arguments[x]]
		if(x!=len(arguments)-1):
			retString+=curObject.xs[x]

	return retString

#z=getDict()
#for x in z:
	#print z[x]
	#pass	
#print(z["tavla"])
#print(getSentenceFromGismu("tavla",["mi","do","balvi"],z,getCmavo()))
# main()
