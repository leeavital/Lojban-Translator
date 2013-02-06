import re, string
class gismu:
	__slots__=['lojbanWord','englishPhrase','xs']
	def __init__(self, lojbanWord,englishPhrase,xs):
	    self.lojbanWord=lojbanWord
	    self.englishPhrase=englishPhrase
	    self.xs=xs
	def __str__(self):
		r=self.lojbanWord+" - "+self.englishPhrase+": "
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
		rest=line[i:]
		if("x1" in rest):
			if(rest[0][0]!="x"):
				rest=line[i+1:]
			s=""

			for z in rest:
				s+=z+" "
			newS=""

			for n in range(10,0,-1):
				if(n==1):
					new=""
					backup=s
					for c in string.punctuation:
						s=s.replace(c," ")
					s=s.replace('/', " ")
					s=s.split()
					for word in s:
						if word in engList:
							newS+=word+" "
						else:
							break
					rest=newS
					rest=rest.split()
					last=rest[len(rest)-1]
					backup=backup.split()
					for word in backup:
						if(last in word):
							new+=word
							rest=new

							break
						else:
							new+=word+" "
					break
				if("x"+str(n) in s):
					rest=s.split("x"+str(n))
					rest=rest[0]+"x"+str(n)
					break

			#At this point we have the word in both languages and "rest"

			rest=re.split("x\d",rest)
			a=rest[1:-1]

			g=gismu(lojbanWord,engWord,a)
			gismuList[lojbanWord]=g
		else:
			later.append(rest)

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
	#print(curObject.xs)

	retString=""
	for x in range(len(arguments)):
		if(arguments[x] in dictionary):
			retString+=dictionary[arguments[x]].englishPhrase
		elif(arguments[x] in dictionary2):
			retString+=dictionary2[arguments[x]]
		else:
			retString+=arguments[x]
		if(x!=len(arguments)-1 or len(arguments)==1):
			s=curObject.xs[x].split("[")[0]
			retString+=s

	return retString

d=getDict()
c=getCmavo()

s=getSentenceFromGismu("barda",["gerku","xunre"],d,c)

print(s)