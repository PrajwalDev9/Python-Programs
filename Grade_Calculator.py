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
if(per>75 and p>=40 and c>=40 and m>=40):
    print("Your Total Marks:",t,"Your Percentage:",per)
    print("You Have Distinction")
elif(60<per<75 and p>=40 and c>=40 and m>=40):
    print("Your Total Marks:",t,"Your Percentage:",per)
    print("You Have First Divsion")
elif(50<per<60 and p>=40 and c>=40 and m>=40):
    print("Your Total Marks:",t,"Your Percentage:",per)
    print("You Have Second Division")
elif(40<=per<50 and p>=40 and c>=40 and m>=40):
    print("Your Total Marks:",t,"Your Percentage:",per)
    print("You Have Third Division")
else:
    print("You have Failed")
