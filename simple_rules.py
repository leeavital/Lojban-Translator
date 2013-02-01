import camxes


def getEnglishTranslation( sentence ):
   """parse a lojban sentence
      return the english translation"""

   rootNode = camxes.parse( sentence )
 
   return translateSentence( rootNode ) 



def translateSentence( rootNode ):
   """get it to translate one level deep"""

   return rootNode




if __name__ == "__main__":
   print getEnglishTranslation( "mi vecnu ti ta" )
   print getEnglishTranslation( "mi ti vecnu ta" )
