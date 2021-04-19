def subsequence(str1):
    if (len(str1)==0):
        return [" "]
    sub_string = subsequence(str1[1:len(str1)])
    result = [" "]* (2*len(sub_string))
    k=0

    for i in range(len(sub_string)):
        result[k] = sub_string[i]
        k=k+1

    for i in range(len(sub_string)):
        result[k] = str1[0] + sub_string[i]
        k=k+1
    print(result)
    return result


subsequence('net')