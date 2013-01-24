import re
def main():
	gismufilename="gismu.txt"
	gismu=getGismu(gismufilename)
	printDict(gismu)



def getGismu(filename):
	d={}
	for line in open(filename):
		if("[" in line and line[0]!="[" and "x1" not in line):
			print(line)
			line=line.split()
			d[line[0]]=line[len(line)-1].replace("'","")

	return d

def printDict(d):
	for key in d:
		print(key+": "+d[key])
main()