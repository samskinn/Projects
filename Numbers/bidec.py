#Create a converter that changes binary numbers to decimals and vice versa 

def b_to_d(number):
  var = str(number)[::-1]
  counter = 0
  decimal = 0
  while counter < len(var):
    if int(var[counter]) == 1:
      decimal += 2**counter
      counter += 1
  return decimal

def d_to_b(number):
  binary = ''
  while number > 0:
    binary += str(number % 2)
    number = number / 2
  return binary[::-1]

print("Enter 0 for binary to decimal conversion")
print("Enter 1 for decimal to binary conversion")

choice = input("Enter the conversion type: ")
if choice == 0:
  number = input("Enter the number: ")
  print("The decimal of %s is %s" % (number, b_to_d(number)))
  
elif choice == 1:
  number = input("Enter the number: ")
  print ("The binary of %s is %s" % (number, d_to_b(number))) 
  
else:
  print("Invalid choice")
