def mergeSort(Slist):
    comparing_time = 0
    swaps = 0
    comparing_time = comparing_time+1
    if len(Slist) > 1:
        mid = len(Slist)//2
        left = Slist[:mid]
        right = Slist[mid:]
        # swaps = swaps + 1

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0
        comparing_time = comparing_time + 1
        while i < len(left) and j < len(right):
            if left[i].number < right[j].number:
                Slist[k] = left[i]
                i = i + 1
            else:
                Slist[k] = right[j]
                j = j + 1
            k = k + 1
            swaps = swaps + 1

        comparing_time = comparing_time + 1
        while i < len(left):
            Slist[k] = left[i]
            i = i + 1
            k = k + 1
            swaps = swaps+1

        comparing_time = comparing_time + 1
        while j < len(right):
            Slist[k] = right[j]
            j = j + 1
            k = k + 1
            swaps = swaps + 1

    print("Total swaps: " + str(swaps))
    print("Total compare: " + str(comparing_time))

# Slist = [64, 4, 58 , 70, 3, 12, 1, 15, 2]
# mergeSort(Slist)
# print(Slist)