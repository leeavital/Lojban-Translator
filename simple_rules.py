import camxes
from gismu_rules import getSentenceFromGismu, getDict, getCmavo
import re


print "Loading the grammar and dictionary (this may take up to a minute)..."
gismuDict = getDict()
cmavoDict = getCmavo()  
print "The grammar was loaded sucessfully"

tree=False
def printG():
   for x in gismuDict:
      print(gismuDict[x])
def printC():
   for x in cmavoDict:
      print(x+": "+cmavoDict[x])


# turn on the prnt flag
def printTree():
   global tree
   tree=True



# return the enlish translation of a lojban sentence
def getEnglishTranslation( sentence ):
   """parse a lojban sentence
      return the english translation"""

   
   # get a list of all the names
   names = [ str(e) for  e in re.findall( r"\.[^\s]*\.", sentence ) ]
   
   
   print names 

   # replace all occurences with "ko"
   sentence = re.sub( r"\.[^\s]*\.", "ko", sentence)
   
    
   # make a parse tree
   rootNode = camxes.parse( sentence )
    
   if tree:
      print rootNode
   
   
   return translateSentence( rootNode, names=names ) 



# translate the word 
def getWordTranslation(word):
   if(word in gismuDict):
      return str(gismuDict[word])
   if(word in cmavoDict):
      return str(cmavoDict[word])
   else:
      return "Word not known"



# get the enslish sentence from the parse tree
def translateSentence( rootNode, names=[] ):
   """get it to translate one level deep"""
   
   
   if names == []:
	  print "there was no name"
   else:
	  print "the name is %s and the sentence is %s" % ( str(names), rootNode.lojban)
    
   # for efficiency
   global gismuDict
      
   # extremely naive 
   threeKoha = rootNode.find( 'KOhA' )
   
   
   theKoha = [ str(x.lojban) for x in threeKoha ]
    
   # hard coded modifiers
   theSe = rootNode.find( 'SE' )
   if theSe != None and len(theSe) > 0 and theSe[0].lojban == 'se':
	  theKoha[0], theKoha[1] = theKoha[1], theKoha[0] 
   
   if theSe != None and len(theSe) > 0 and theSe[0].lojban == 'te':
	  theKoha[0], theKoha[2] = theKoha[2], theKoha[0]
   
   if theSe != None and len(theSe) > 0 and theSe[0].lojban == 've':
	  theKoha[0], theKoha[3] = theKoha[3], theKoha[0]

       
    
   oneGismu = rootNode.find( 'gismu' )
  
   gismu1 = str( oneGismu[0].lojban )
   
   namesI = 0 
   for i in range( len(theKoha) ):
	  if theKoha[i] == "ko"  and not names == []:
		 theKoha[i] = names[namesI]
		 namesI += 1 
   
   return getSentenceFromGismu( gismu1, theKoha, gismuDict, cmavoDict ) 




if __name__ == "__main__":
   print getEnglishTranslation( "mi vecnu ti ta" )
   print getEnglishTranslation( "mi ti vecnu ta" )
