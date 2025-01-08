L = int(input())
list = []
for _ in range(L):
    x,y = map(str, input().split())
    for i in range(int(x)):
        list.append(y)
    print(''.join(list))
    list = []