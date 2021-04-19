def removeDuplicate(str1):

    output = ""

    for i in str1:
        if i in output:
            pass
        else:
            output += i
    print(output)

removeDuplicate("aaabbbcccdddeee")