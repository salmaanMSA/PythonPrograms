# Method 1 :  Without using Counter Libarary

str1 = "Python Programming"
duplicate = set()

for i in str1:
    if str1.count(i) > 1 :
        duplicate.add(i)

print(duplicate)

# Method 2: With using Counter Library

from collections import Counter

word_length = Counter(str1)

for key, value in word_length.items():
    if value > 1:
        print(f'{key} occurs {value} times in {str1}')
