import re

def findSpecialChar(str1):

    my_str = re.compile('[!@#$%^&*()?/~]')

    if (my_str.search(str1) == None):
        print("The given string not have special character")
    else:
        print("The given string contain special character")

# findSpecialChar("hello@#")

str2 = "Hello"

if str2.isalpha() == True:
    print("The given string do not contains digit")
else:
    print("The given string contains digit")


