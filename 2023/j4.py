n = int(input())
count = 0
row1 = [int(i) for i in input().split()]
row2 = [int(i) for i in input().split()]


for i in range(len(row1)):
    if i - 1 != -1:
        before = i-1
    else:
        before = i
    if i + 1 != len(row1):
        after = i+1
    else:
        after = i

    if row1[i] == 1 and row1[after] == 1 and row1[before] == 1 and after > i and before < i:
        count += 1
    elif row1[i] == 1 and row1[after] == 1  and after > i or row1[i] == 1 and row1[before] == 1 and before < i:
        count += 2
    elif row1[i] == 1:
        count += 3

    if row2[i] == 1 and row2[after] == 1 and row2[before] == 1 and after > i and before < i:
        count += 1
    elif row2[i] == 1 and row2[after] == 1  and after > i or row2[i] == 1 and row2[before] == 1 and before < i:
        count += 2
    elif row2[i] == 1:
        count += 3

    if row2[i] == 1 and row1[i] == 1 and i % 2 == 0:
        count -= 2

print(count)