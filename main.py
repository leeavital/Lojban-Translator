def main():
	gismufilename="gismu.txt"
	gismu=getGismu(gismufilename)
	printDict(gismu)



def getGismu(filename):
	d={}
	i=1
	for line in open(filename):
		i+=1
		if(i%3==1):
			print(line)

			line=line.split()
			
			d[line[0]]=line[:-1]

	return d

def printDict(d):
	for key in d:
		print(key+": "+d[key])
main()