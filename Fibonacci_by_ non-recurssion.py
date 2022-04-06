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
    a=0;
    print(a)
    b=1;
    print(b)
    for i in range(n-2):
        c=a+b;
        a=b;
        b=c;
        print(c);
a=int(input("Enter a Range:"))
n=fib(a);


