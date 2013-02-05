import camxes
from gismu_rules import getSentenceFromGismu, getDict, getCmavo



print "loading the grammar (this may take up to a minute)..."
gismuDict = getDict()
cmavoDict = getCmavo()  
print "the grammer was loaded"




def getEnglishTranslation( sentence ):
   """parse a lojban sentence
      return the english translation"""

   rootNode = camxes.parse( sentence )
  
    
   return translateSentence( rootNode ) 



def translateSentence( rootNode ):
   """get it to translate one level deep"""
   
   # for efficiency
   global gismuDict

   
   print rootNode
      
   # extremely naive 
   threeKoha = rootNode.find( 'KOhA' )
   
   
   theKoha = [ str(x.lojban) for x in threeKoha ]
   
   
   theSe = rootNode.find( 'SE' )
   if theSe != None and len(theSe) > 0 and theSe[0].lojban == 'se':
      theKoha[0], theKoha[1] = theKoha[1], theKoha[0] 
   
    
    
   oneGismu = rootNode.find( 'gismu' )
  
   gismu1 = str( oneGismu[0].lojban )
   
   
   print gismu1
       
   return getSentenceFromGismu( gismu1, theKoha, gismuDict, cmavoDict ) 

   # return sumti[koha1] + gismuDict[gismu1] + sumti[koha2] + " from " + sumti[koha3]




if __name__ == "__main__":
   print getEnglishTranslation( "mi vecnu ti ta" )
   print getEnglishTranslation( "mi ti vecnu ta" )
