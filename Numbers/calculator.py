"""
create a calculator
function for adding, subtracting, dividing, and multiplying. 
"""
import math

def add(num1, num2):
  num1 = int(input(" "))
  num2 = int(input(" "))
  result = num1 + num2
  print result
  
def sub(num1, num2):
  num1 = int(input(" "))
  num2 = int(input(" "))
  result = num1 - num2
  print result
  


def div(num1, num2):
  num1 = int(input(" "))
  num2 = int(input(" "))
  result = num1 / num2
  print result
  


def mul(num1, num2):
  num1 = int(input(" "))
  num2 = int(input(" "))
  result = num1 * num2
  print result 
  
  

def sqr(num1):
  num1 = int(input(" "))
  result = num1 ** 2
  print result
  
 

def prc(num1):
  num1 = int(input(" "))
  result = num1 / 100
  print result
  


def log(num1):
  num1 = int(input(" "))
  result = math.log10(num1)
  print result
  
 

  
