def removeChar(str1, char):
    str2 = list(str1)
    str2.remove(char)

    return ''.join(str2)



str1 = input("Enter a String:")
char = input("Enter the charcter to be removed from the string:")
res = removeChar(str1, char)
print(res)


