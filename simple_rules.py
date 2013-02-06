import camxes
from gismu_rules import getSentenceFromGismu, getDict, getCmavo



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
def printTree():
   global tree
   tree=True
def getEnglishTranslation( sentence ):
   """parse a lojban sentence
      return the english translation"""

   rootNode = camxes.parse( sentence )
  
   if tree:
      print rootNode
   return translateSentence( rootNode ) 

def getWordTranslation(word):
   if(word in gismuDict):
      return str(gismuDict[word])
   if(word in cmavoDict):
      return str(cmavoDict[word])
   else:
      return "Word not known"
def translateSentence( rootNode ):
   """get it to translate one level deep"""
   
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
   
   
       
   return getSentenceFromGismu( gismu1, theKoha, gismuDict, cmavoDict ) 



if __name__ == "__main__":
   print getEnglishTranslation( "mi vecnu ti ta" )
   print getEnglishTranslation( "mi ti vecnu ta" )
