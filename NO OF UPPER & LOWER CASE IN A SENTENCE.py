a= input("ENTER THE SENTENCE=")
b=0
c=0
for i in a:
    if ord(i)>=92 and ord(i)<=122:
        b=b+1
    elif ord(i)>=65 and ord(i)<=90:
        c=c+1
print("No of Lower case =",b)
print("No of Upper case =",c)
    
