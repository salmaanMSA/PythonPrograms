def checKRotation(str1, str2):
    if len(str1) != len(str2):
        print("Length of two string are different so they cannot rotation of each other")

    temp = str1 + str1

    if (str2 in temp):
        print("The given two string are rotation of each other")
    else:
        print("Thre given strings are not rotation of each other")


checKRotation("ANU","NUA")
