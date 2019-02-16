"""
User enters cost, amount of money given. Calculate change in quarters, dimes, nickels, pennies
"""


cost = float(raw_input("What is the cost of the product? "))
tender = float(raw_input("How much money are you giving to buy the product? "))

while cost < tender:
  print "You still owe $%.2f" % (cost - given)

change = (cost - tender) * 100
quart = 0
dime = 0
nickel = 0
penn = 0

if change >= 25:
  quart = int(change / 25)
  change = change % 25
  
if change >= 10:
  dime = int(change / 10)
  change = change % 10
  
if change >= 5:
  nickel = int(change / 5)
  change = change % 5
  
if change >= 1:
  penn = change
