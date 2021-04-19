from math import factorial

# Method 1 : Without Using Permutation Library

def lexicographical_permutations1(str):
    # there are going to be n ! permutations where n = len(seq)
    for p in range(factorial(len(str))):
        print(''.join(str))

        i = len(str) - 1

        # find i such that str[i:] is the largest sequence with
        # elements in descending lexicographic order
        while i > 0 and str[i - 1] > str[i]:
            i -= 1

        # reverse str[i:]
        str[i:] = reversed(str[i:])

        if i > 0:

            q = i
            # find q such that str[q] is the smallest element
            # in str[p:] such that str[q] > str[i - 1]
            while str[i - 1] > str[q]:
                q += 1

            # swap str[i - 1] and str[q]
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp


s = 'abcd'
s = list(s)
s.sort()
lexicographical_permutations1(s)

# Method2: With using permutation Library

from itertools import permutations

def lexcicographical_permutation2(str1):

    perm = sorted(''.join(char) for char in permutations(str1))

    for x in perm:
        print(x)

lexcicographical_permutation2("xyz")