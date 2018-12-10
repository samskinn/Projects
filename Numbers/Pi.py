# Find Pi to the nth digit
""" Pi is already a present in Python
Need to import the Math function to call
"""

import math

def defining_pi(roundVal):
  ori_pi = round(math.pi, roundVal)
  pi = str(ori_pi)
  return ori_pi;

roundTo = raw_input("Enter how many decimal places of Pi you want: ")
try:
  roundint = int(roundTo)
  if roundint > 50:
    print "Integer selected is too large"
  else:
    print defining_pi(roundint)
  except:
  print "You did not enter an integer"
