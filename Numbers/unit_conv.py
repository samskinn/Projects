""" 
Unit Conversion
Try and make it work back and forth between units
temp, currency, mass, volume, length
"""

import os, json
from urllib2 import urlopen

os.system('clear')

CONVERT_TO = {
  'volume': {
    'tsp': 48,
    'tbsp': 16,
    'c': 1,
    'q': .25,
    'p': .5,
    'gal': .0625,
    'oz': 8
  },
  
  'mass': {
    'g': 453.59,
    'oz': 16,
    'lb': 1,
    'kg': 0.453592
    
  },
  
  'length': {
    'm': 1,
    'ft': 3.28084,
    'in': 39.3701,
    'yd': 1.09361
  }
}


CONVERT_FROM = {
  'volume': {
    'tsp': .015625,
    'tbsp': .0625,
    'c': 1,
    'q': 4,
    'p': 2,
    'gal': 16,
    'oz': .125
  },
  'mass': {
    'g': .0022046,
    'oz': .0625,
    'lb': 1,
    'kg': 2.2406
  },
  'length': {
    'm': 1, 
    'ft': .3048,
    'in': .0254,
    'yd': .9144
  }
}


def temp():
  print """\n1: Celsius to Fahrenheit
    2. Celsius to Kelvin
    3. Fahrenheit to Celsius
    4. Fahrenheit to Kelvin
    5. Kelvin to Celsius 
    6. Kelvin to Fahrenheit"""
  
    choice = int(input("Enter conversion type: "))
    
    if choice == 1:
      degrees = int(input("Enter temperature to convert: "))
      result = (degrees * 1.8) + 32
      unit = 'F'
     
    elif choice == 2:
      degrees = int(input("Enter temperature to convert: "))
      result = degrees + 273.15
      unit = 'K'
      
    elif choice == 3:
      degrees = int(input("Enter temperature to convert: "))
      result = (degrees - 32) / 1.8
      unit = 'C'
      
    elif choice == 4:
      degrees = int(input("Enter temperature to convert: "))
      result = ((degrees - 32) / 1.8) + 273.15
      unit = 'K'
      
    elif choice == 5:
      degrees = int(input("Enter temperature to convert: "))
      result = degrees - 273.15
      unit = 'C'
      
    elif choice = 6:
      degrees = int(input("Enter temperature to convert: "))
      result = ((degrees -273.15) * 1.8) + 32
      unit = 'F'
      
    else: 
      print "Invalid selection"
      temp()
      
    print "Value: " + str(result) + ' ' + unit
                              
def do_convert(conversion):
  conversion_units = ','.join(CONVERT_FROM[conversion].keys())
  amount = float(input("Enter conversion amount:"))
  source_unit = input("Enter source unit(%s):" % conversion_units)
  to_unit = input("Enter unit to convert to (%s):" % conversion_units)
  
  print "%s %s's equals %f %s's" % (amount, source_unit, amount * \ 
                                    CONVERT_FROM[conversion][source_unit] * \
                                    CONVERT_TO[conversion][to_unit], to_unit)
  
def currency():
  amount = str(input("Enter amount to convert: "))
  from_currency = str(input("Enter your source currency(3 digit code): "))
  to_currency = str(input("Enter the currency you would like to convert to(3 digit code): "))
  
  request = urlopen('http://rate-exchange.appspot.com/currency?from=' + from_currency + '&to=' + to_currency + '&q=' + amount)
  response = json.loads(request.read())
  
  print("%s %s is equal to %f %s" % (amount, from_currency, float(response['v']), to_currency))
  
                                     
print """1: Temperature
2: Volume
3: Mass
4: Length
5: Currency"""

input = input("Enter conversion type: ")

if input == 1:
  temp()
elif input == 2:
  do_convert('volume')
eilf input == 3:
  do_convert('mass')
elif input == 4:
  do_convert('length')
elif input == 5:
  currency()
else:
  print ("Invalid selection")
                                     
                                     
  
                                 
  
                              
                         
    
    
    
