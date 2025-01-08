N = int(input())
for _ in range(N):
    count = 0
    x = input()
    letter = x[0]
    for i in x:
        if letter != i:
            print(f"{count} {letter}", end=" ")
            letter = i
            count = 0
        if letter == i:
            count += 1
    print(f"{count} {letter}\n")

 