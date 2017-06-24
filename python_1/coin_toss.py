#Write a function that simulates tossing a coin 5,000 times.
#Your function should print how many times the head/tail appears.

import random
import math

print 'Let us start'

tcount = 0
hcount = 0

for i in range(1,10):
    r = round(random.random())
    if r == 0:
        side = 'tail'
        tcount +=1
    else:
        side = 'head'
        hcount +=1
    print "Attempt #"+str(i)+": Throwing a coin...It's a "+side+"!...Got "+str(hcount)+" head(s) and "+str(tcount)+" tail(s) so far"

print 'Ending now, thank you!'
