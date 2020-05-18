# find e to the Nth digit

"""
express e in a function and run it through a check that works out the decimal places
"""

import math

def ori_exp(roundVal):
  x = 1
  the_exp = round(math.exp(x), roundVal)
  

roundTo = raw_input("How many decimal places of e do you require? ")
try:
  roundint = int(roundTo)
  if roundint > 30:
    print "The value chosen is too high, select a lower number."
  else: 
    print(ori_exp(roundint))
  except:
    print("You haven't entered an integer")
