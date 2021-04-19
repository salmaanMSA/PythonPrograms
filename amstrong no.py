num=int(input("ENTER THE NUMBER:"))
sum=0
temp=num

while temp>0:
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10

if (num==sum):
    print("It is amstrong number")
        
else:
    print("It is not an amstrong number")
    
