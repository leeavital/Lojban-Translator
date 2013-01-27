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


print bridi_3.parseString(" mi vecnu ti ta ")
