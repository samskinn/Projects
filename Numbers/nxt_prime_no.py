#Finding the nex prime no until user chooses to stop

user_int = raw_input("Do you want to keep finding prime numbers (y/n)? ")
start = 1

def prime_number(n):
  if  n % 2 == 0:
    return False
  
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False
    
    return True
  
  
while user_int.lower().startswith('y'):
  start += 1
  
  while prime_number(start) == False:
    start += 1
    
    print "The next prime number is: " + str(start)
    user_int = raw_input("Do you want to keep finding prime numbers (y/n)? ")
