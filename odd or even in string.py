a= input("ENTER A STRING=")
for i in range(len(a)):
    if(i%2==0):
        print('EVEN INDEX=',i,a[i])
    else:
        print('ODD INDEX=',i,a[i])
