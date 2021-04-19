str1 = input("Enter The String1:")
str2 = input ("Enter The String2:")


if (len(str1) == len(str2)):
    if sorted(str1) == sorted(str2):
        print("The given string is Anagram")
    else:
        print("The given string is not anagram")

else:
    print("The length of entered strings are not equal, so they are not anagram")
