N = int(input())
max= 0
winner = ""
for _ in range(N):
    a = input()
    b = int(input())
    if b > max:
        max = b
        winner = a
print(winner)

