from pyparsing import Literal, Word, Optional, Combine, delimitedList, printables, alphanums

def getString():
	gismufilename="gismu.txt"
	gismu=getGismu(gismufilename)
	#printDict(gismu)
	gismuList=[]
	for x in gismu:
		gismuList.append(x)


	s=""

	for z in gismuList:
		s+="Literal(\""+z+"\") ^ "
	s=s[:len(s)-2]
	print(s)
	return s
def getGismu(filename):
	d={}
	for line in open(filename):
		if("[" in line and line[0]!="[" and "x1" not in line):
			#print(line)
			line=line.split()
			d[line[0]]=line[len(line)-1].replace("'","")

	return d

main()
