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
p=int(input("Enter Marks in Physics:"))
c=int(input("Enter Marks in Chemistry:"))
m=int(input("Enter Marks in Maths:"))
t=p+c+m;
per=t*100/300;
if(per>75):
    if(p<=40):
        if(c<=40):
            if(m<=40):
                print("You Have Distinction")
elif(60<per<75):
    if(p<=40):
        if(c<=40):
            if(m<=40):
                print("You have First Division")
else:
    print("You Have Failed")