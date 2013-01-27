import re
def main():
	print("Welcome to Ben, Zach and Lee's Lojban Translator\nEnter a word or phrase in lojban to continue.\nEnter \"exit\" to quit.")
	i=""
	while(i!="exit"):
		i=raw_input()
		if(i=="exit"):
			break
		t=translate(i)
		print(t)
	print("Thanks for using our software!  Go fuck yourself!")
def translate(t):
	return "Penis"
main()
