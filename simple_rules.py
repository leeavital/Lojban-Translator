from pyparsing import *


# here are the rules

# literal rules for gismu (the simplest words with meaning)
gismu = Literal("mi") ^ Literal("ta") ^ Literal("ti")


# a sumti can be a gismu (or other things, but only gismu for now)
sumti = gismu 


selbri = Literal("vecnu")


# there are three forms of a bridi/3
bridi_3 = ( sumti + selbri + sumti + sumti ) 
bridi_3 ^= ( selbri + sumti + sumti + sumti )
bridi_3 ^= ( sumti + sumti + sumti + selbri )
bridi_3 ^= ( sumti + sumti + selbri + sumti )



sumti ^= bridi_3

lojban_sentence = LineStart() + (bridi_3) + LineEnd()




def bridi_3_parse( s ):
   return lojban_sentence.parseString( s )

def parse( s ):   
   
   try:
      return bridi_3_parse( s )

   except:
      print "cannot parse: %s" % s




print parse( "mi vecnu ti mi vecnu ti mi" )
