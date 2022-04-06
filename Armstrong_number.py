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

def main():
    pass

if __name__ == '__main__':
    main()
temp=0
n=int(input("Enter a Number:"))
temp=n;
sum=0;
while(n>0):
    cube=(n%10)*(n%10)*(n%10);
    sum=sum+cube;
    n=n//10;
    print(n)

if(sum==temp):
    print("It is an Armstrong Number")
else:
    print("It is not a Armstrong Number")