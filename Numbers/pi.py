# Find Pi to the nth digit
""" Pi is already a present in Python
Need to import the Math function to call
"""

import math

def defining_pi(roundVal):
  ori_pi = round(math.pi, roundVal)
  pi = str(ori_pi)
  return ori_pi;

round_to = raw_input("Enter how many decimal places of Pi you want: ")
try:
  round_int = int(roundTo)
  if round_int > 50:
    print "Integer selected is too large"
  else:
    print defining_pi(round_int)
  except:
  print "You did not enter an integer"