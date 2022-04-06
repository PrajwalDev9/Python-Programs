#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Prajwal
#
# Created:     31/01/2020
# Copyright:   (c) Prajwal 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fib(n):
    if n<=1:
        return 1;
    else:
        return(fib(n-1)+fib(n-2));
n=int(input("Enter the Range: "))
print("Fibonacci Series is:\n0")
for i in range(n-1):
    print(fib(i))
