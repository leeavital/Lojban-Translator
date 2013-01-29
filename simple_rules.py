from pyparsing import *


sentence =  Forward()
terms = Forward()
bridi_tail = Forward()
bridi_tail_1 = Forward() 
bridi_tail_2 = Forward()
bridi_tail_3 = Forward()
selbri = Forward()
tail_terms = Forward()


sentence << ZeroOrMore(terms) + bridi_tail
bridi_tail << bridi_tail_1
bridi_tail_1 << bridi_tail_2
bridi_tail_2 << bridi_tail_3
bridi_tail_3 << selbri + tail_terms

