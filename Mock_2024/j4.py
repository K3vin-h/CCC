#not Finished
N, K = list(map(int, input().split()))  
x = input()
i = 0
x = list(x)
a =[] 
r=[]
while i < len(x) - 1:
    if x[i] == "1" and x[i+1]== "1":
        x[i] = "0"
    i += 1
for _ in range(K):
    b = -1
    max = -1
    for i in range(len(x)):
        if x[i] == "0":
            temp = x.copy()
            temp[i] = "1"
            merges = 0
            j = 0
            while j < len(temp) - 1:
                if temp[j] == "1" and temp[j+1] == "1":
                    temp[j] = "0"
                    merges += 1
                j += 1  
            a.append(merges)
            r.append(i)
            if merges > max:
                max = merges
                b = i

    if b != -1:
        x[b] = "1"
i = 0
while i < len(x) - 1:
    if x[i] == "1" and x[i+1] == "1":
        x[i] = "0"
    i += 1
print(a, r)
print(x.count("1"))
