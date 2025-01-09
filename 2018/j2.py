N = int(input())
yes = input()
tod = input()
x = []
y = []
for i in yes:
    x.append(i)
for i in tod:
    y.append(i)


count = 0

for i in range(N):
    if x[i] == "C" and y[i] == "C":
        count += 1
print(count)