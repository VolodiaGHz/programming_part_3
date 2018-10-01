import time
from Lab_1.Stadium import Stadium
from Lab_1.Merge_sort import mergeSort


def bubbleSort(Slist):
    print("Bubble sort:")
    comparing_time = 0
    swaps = 0
    for i in range(len(Slist)-1, 0, -1):
        comparing_time = comparing_time + 1
        for j in range(i):
            if Slist[j].power > Slist[j+1].power:
                temp = Slist[j]
                Slist[j] = Slist[j+1]
                Slist[j+1] = temp
                swaps = swaps+1
    print("Comparing time: " + str(comparing_time))
    print("Total swaps: " + str(swaps))




if __name__ == "__main__":
    print("--------")
    Slist = []
    name = 0
    number_of_viewers = 1
    power_of_ligthing = 2
    file = open('Stadium_List')
    for line in file:
        values = line.split(',')
        stadium = Stadium(int(values[number_of_viewers]), values[name], int(values[power_of_ligthing][:-1]))
        Slist.append(stadium)
    for item in Slist:
        print(item)

    # Stadium_list = [2, 5, 1, 99, 3, 4, 65, 54, 67, 12, 10, 7]
    sort_time = time.perf_counter()
    # Slist = Stadium_list
    bubbleSort(Slist)
    print("Time of sorting: " + str(time.perf_counter() - sort_time))
    print(Slist)
    for stadium in Slist:
        print(stadium)
    print("--------")

    print("Merge sort: ")
    sort_time = time.perf_counter()
    mergeSort(Slist)
    print("Time of sorting: " + str(time.perf_counter() - sort_time))
    print(Slist)
    for stadium in Slist:
         print(stadium)

    print("--------")
