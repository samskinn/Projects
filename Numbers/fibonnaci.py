# generate a Fibonnaci code that can generate the number of the nth sequence.

import math

n = int(input("Enter the number of the Fibonnaci sequence required: "))

x = 0
y = 1

counter = 0

if n < 0:
  (print "Error! Please enter a posstive integer value")
elif n == 0:
  print ("Fibonnaci number is 0")
elif n == 1:
  print ("Fibonnaci number  is 0")
else: 
  print ("Fibonnaci number is " + "%d" % n)
  while counter < n:
    fib = x + y
    x = y 
    y = fib
    count += 1
    print(fib[n])
    
   
