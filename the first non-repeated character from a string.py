# Method 1 : Without USing counter library
str1 = "Python Programming"
char = set()
for i in str1:
    if str1.count(i) == 1:
        char.add(i)

print(char)


# Method 2: With Counter Library

from collections import Counter

char = Counter(str1)
list_1 = []

for k, v in char.items():
    if v == 1:
        list_1.append(k)
print(list_1)

