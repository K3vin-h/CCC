list = []
x = map(int, input().split())
list = [0, *x]
city = 0
new_list = []
new_list2 = []
distance = []
sum = 0
while city != 5:

    for i in range(len(list)):
        if i <= city:
            new_list.append(list[i])
        else:
            new_list2.append(list[i])
    new_list.pop(0)
    new_list.reverse()
    for i in range(len(new_list)):
        sum += int(new_list[i])
        distance.append(sum)
    sum = 0
    distance.reverse()
    distance.append(0)
    sum2=0
    for i in range(len(new_list2)):
        sum2 += int(new_list2[i])
        distance.append(sum2)
        # pass
    city += 1
    new_list = []
    new_list2 = []
    print(" ".join(map(str, distance)))
    distance = []

