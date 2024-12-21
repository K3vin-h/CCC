size = int(input())
size1 = size
while True:
    r = int(input())
    if size1 > r:
        size1 = size1+r
    else:
        break
print(size1)