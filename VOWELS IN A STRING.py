a=input("ENTER THE SENTENCE=")
b= ["a","e","i","o","u","A","E","I","O","U"]
c=0
for char in a:
    if char in b:
        c=c+1
print("The number of vowels in a=",c)
