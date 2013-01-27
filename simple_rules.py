from pyparsing import *


# here are the rules

# forwand declarations
lojban_sentence = Forward()
sumti = Forward()
selbri = Forward()
bridi_3 = Forward()


lojban_sentence <<  ( LineStart() + bridi_3 + LineEnd() )



# literal rules for gismu (the simplest words with meaning)
gismu = Literal("mi") ^ Literal("ta") ^ Literal("ti")


# a sumti can be a gismu (or other things, but only gismu for now)
sumti << gismu ^ bridi_3


selbri <<  Literal("vecnu")


# there are three forms of a bridi/3
bridi_3 <<  ( sumti + selbri + sumti + sumti ) 
bridi_3 ^=  ( selbri + sumti + sumti + sumti )
bridi_3 ^=  ( sumti + sumti + sumti + selbri )
bridi_3 ^=  ( sumti + sumti + selbri + sumti )






def parse( s ): 
   
   try:
      return lojban_sentence.parseString( s ) 

   except:
      print "cannot parse: %s" % e




print parse( "mi vecnu ta ti" )
print parse("mi vecnu ta mi vecnu ta ti")
