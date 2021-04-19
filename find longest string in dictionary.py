def isSubsequence(str1,str2):

    m = len(str1)
    n = len(str2)

    j = 0  # index for str1
    i = 0  # index for str2

    while (j < m and i < n):

        if (str1[j] == str2[i]):
            j+=1
        i+=1
    return (j == m)

def findLongestString(dict1, str1):

    result =""
    length = 0

    for word in dict1:
        if (length < len(word) and isSubsequence(word, str1)):
            result = word
            length = len(word)
    return result

dict1 = {"ale", "apple", "monkey", "plea"}
str1 = "abpcplea"

print(findLongestString(dict1,str1))