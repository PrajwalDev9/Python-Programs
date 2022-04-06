#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Prajwal
#
# Created:     21-01-2020
# Copyright:   (c) Prajwal 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
num=int(input("Enter a number: "))
rev=0;
while(num>0):
    rev=rev*10+num%10;
    num=num//10;
print("Reverse number is: ",rev)
