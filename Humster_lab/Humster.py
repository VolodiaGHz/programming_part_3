
hum_info = []
bas_info = []

def open_food():
    with open('Humster.txt') as Text:
        for line in Text:
            values = line.split(",")
            if len(values) == 1:
                hum_am = 1
                bas_info.append(int(values[0][0:]))
            elif len(values) == 2:
                hungry = 0
                greed = 1
                hum_info.append([int(values[0]), int(values[1][:1])])

                
Sum = []
hum_am = 1
def formula():
    for i in hum_info:
        test = i[0] + i[1] * (bas_info[hum_am] - 1)         # =========== #
        Sum.append(test)                                    # It is       #
        max_el = max(Sum)                                   # A           #
        Tot_f = bas_info[0]                                 # Suma with   #
        if max_el > Tot_f:                                  # Formula     #
            Max = Sum.index(max_el)                         # =========== #
            Sum.pop(Max)
            bas_info[hum_am] = bas_info[hum_am] - 1
            

def Sorting():
    for i in range(len(Sum) - 1, 0, -1):                # =========== #
        for j in range(i):                              # It is       #
            if Sum[j] > Sum[j + 1]:                     # A           #
                temp = Sum[j]                           # Bubble      #
                Sum[j] = Sum[j + 1]                     # sort        #
                Sum[j + 1] = temp                       # =========== #



def couting_total_humsters(Sum):
    Sorting()
    food_count = 0
    Sume = 0
    amount = 0
    if len(Sum) == 0:
        f = open("Hamster.out", 'w')
        f.write("No food - No humsters!")
        f.close()
        # print("No food - No humsters!")
    else:
        if len(Sum) == 2:  # Counting humsters
            if Sum[0] + Sum[1] <= bas_info[0]:
                amount = 2;

            elif Sum[0] + Sum[1] > bas_info[0]:
                if Sum[0] < bas_info[0]:
                    amount = 1
            # print(amount)
        elif len(Sum) == 1:
            if Sum[0] <= bas_info[0]:
                amount = 1
        else:
            for i in range(len(Sum) - 1, 0, -1):
                for j in range(i):
                    if (food_count + Sum[j + 1]) == bas_info[0]:
                        amount = amount + (j + 1)
                    if food_count < bas_info[0]:
                        food_count = food_count + Sum[j] + Sum[j + 1]
                        j = j + 1
                        amount = j + 1
                    if (food_count + Sum[j]) < bas_info[0]:
                        amount = amount + 1
                if food_count < bas_info[0]:
                    amount = Sum.index(max(Sum)) + 1

    print(Sum)
    print("Total available humsters: ")
    print(amount)
    print(food_count)
    f = open("Humster.out", 'w')
    f.write("Total available humsters: " + str(amount))
    f.close()

    if bas_info[0] <= 0:
        # print("No food - No humsters!")
        f = open("Humster.out", 'w')
        f.write("No food - No humsters!")
        f.close()

if __name__ == "__main__":
    with open('Humster.txt') as Text:
        for line in Text:
            values = line.split(",")
            if len(values) == 1:
                hum_am = 1
                bas_info.append(int(values[0][0:]))
            elif len(values) == 2:
                hungry = 0
                greed = 1
                hum_info.append([int(values[0]), int(values[1][:1])])

    formula()
    Sorting()
    couting_total_humsters(Sum)
