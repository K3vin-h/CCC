N =int(input())
k = int(input())
sum = 0
for _ in range(k+1):
    sum += N
    N *= 10
print(sum)