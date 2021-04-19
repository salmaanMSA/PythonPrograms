def lexicographicalSort(str1):
    split_word = str1.split()
    split_word.sort()

    for word in split_word:
        print(word)

lexicographicalSort("Hello this is example how to sort " \
              "The word in alphabetical manner")


