import camxes


gismuDict = {
   "vecnu": "buy"
}


sumti = {
   "mi": "I",
   "ta": "that",
   "ti": "this"
}


def getEnglishTranslation( sentence ):
   """parse a lojban sentence
      return the english translation"""

   rootNode = camxes.parse( sentence )
  
    
   return translateSentence( rootNode ) 



def translateSentence( rootNode ):
   """get it to translate one level deep"""


   
   # extremely naive 
   threeKoha = rootNode.find( 'KOhA' )
   
   koha1 = str( threeKoha[0].lojban )
   koha2 = str( threeKoha[1].lojban ) 
   koha3 = str( threeKoha[2].lojban ) 
   
   oneGismu = rootNode.find( 'gismu' )
  
   gismu1 = oneGismu[0].lojban

   

   return sumti[koha1] + gismuDict[gismu1] + sumti[koha2] + " from " + sumti[koha3]




if __name__ == "__main__":
   print getEnglishTranslation( "mi vecnu ti ta" )
   print getEnglishTranslation( "mi ti vecnu ta" )
