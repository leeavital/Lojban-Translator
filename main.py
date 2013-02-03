import re
from simple_rules import getEnglishTranslation

"""
Here is the main driver
"""

 
def main():
	print("Welcome to Ben, Zach and Lee's Lojban Translator\nEnter a word or phrase in lojban to continue.\nEnter \"exit\" to quit.")
	i= ""
	while i != "exit":
		i = raw_input()
		if i == "exit":
			break
		t = getEnglishTranslation(i)
		print t




main()
