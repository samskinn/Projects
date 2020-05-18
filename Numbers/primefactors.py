# finding out the prime factors of number inputed by user.

import math

n = int(input("Enter any integer to find its prime factors: "))

print("Factors are: ")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1  
