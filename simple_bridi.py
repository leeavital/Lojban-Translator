from pyparsing import *


# here are the rules

# literal rules for gismu (the simplest words with meaning)
gismu = Literal("mi") ^ Literal("ta") ^ Literal("ti")


# a sumti can be a gismu (or other things, but only gismu for now)
sumti = gismu








