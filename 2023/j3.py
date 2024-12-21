n = int(input())
d1 = 0
d2 = 0
d3 =0
d4 =0
d5=0
count = 0
list = []
for _ in range(n):
    x = input()
    if count == 5:
        count = 0
    while count < 5:
        if x[count] == "Y":
            if count == 0:
                d1 += 1
            elif count == 1:
                d2 += 1
            elif count == 2:
                d3 += 1
            elif count == 3:
                d4 += 1
            elif count == 4:
                d5 += 1
        count += 1

list.append(d1)
list.append(d2)
list.append(d3)
list.append(d4)
list.append(d5)

answer = []
max = max(list)
for i in range(5):
    if list[i] == max:
        if i == 0:
            answer.append("1")
        elif i == 1:
            answer.append("2")
        elif i == 2:
            answer.append("3")
        elif i == 3:
            answer.append("4")
        elif i == 4:
            answer.append("5")
ans = ",".join(answer)
print(ans)