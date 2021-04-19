def merge_sort(list1):
    if len(list1) > 1:
        mid_value = len(list1) // 2
        left_list = list1[:mid_value]
        right_list = list1[mid_value:]
        merge_sort(left_list)
        merge_sort(right_list)

        i = 0 # Index for left_list
        j = 0 # Index for right_list
        k = 0 # Index for sorted_list

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
                k += 1

            else:
                list1[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1



num = int(input("Enter the number of element required in a list:"))
list1 = [int(input(f"Enter the element {x}:")) for x in range(num)]
print("Unsorted List:",list1)
merge_sort(list1)
print("Sorted List:",list1)