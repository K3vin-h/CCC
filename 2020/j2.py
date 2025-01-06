P = int(input())
N = int(input())
R = int(input())
sum = N
day = 0
while sum <= P:
    day += 1
    N *= R
    sum += N

print(day)