import re,sys
from simple_rules import *

"""
Here is the main driver
"""

 
def main(argv):
	wordMode=False
	if("-w" in argv):
		wordMode=True
	if("-g" in argv):
		printG()
	if("-c" in argv):
		printC()
	if("-tree" in argv):
		printTree()

	print("\n\n\nWelcome to Ben, Zach and Lee's Lojban Translator\nEnter a word or phrase in lojban to continue.\nEnter \"exit\" to quit.")
	i= ""
	while i != "exit":
		i = raw_input()
		if i == "exit":
			break
		if(wordMode):
			t=getWordTranslation(i)
		else:
			t = getEnglishTranslation(i)
		print t




main(sys.argv)
