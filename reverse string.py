# Method 1 : Using for loop
def reverse(str1):
    reverse_string = ""
    for i in str1:
        reverse_string = i + reverse_string
    print(reverse_string)

reverse("Hello")

# Method 2: USing slicing method
str1 = "Python"
rev_string = str1[::-1]
print(rev_string)

# Method 3: Using recursive function
def reverse_str(str1):

    if len(str1) == 1:
        return str1
    else:
        return  reverse_str(str1[1:])+str1[0]

rev = reverse_str("Django")
print(rev)