N = int(input())
a = []
b = []
for _ in range(N):
    x,y = map(int, input().split(","))
    a.append(x)
    b.append(y)

min_x = min(a)
max_x = max(a)
min_y = min(b)
max_y = max(b)
print(f"{min_x-1},{min_y-1}")
print(f"{max_x+1},{max_y+1}")