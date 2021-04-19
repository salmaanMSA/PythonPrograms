a= int(input("ENTER THE YEAR="))
if(a%4!=0):
    print("THE GIVEN YEAR IS  NOT A LEAP YEAR")
elif(a%4==0 and a%100==0 and a%400==0):
    print("THE GIVEN YEAR IS A LEAP YEAR")
else:
    print("THE GIVEN YEAR IS NOT  A LEAP YEAR")
