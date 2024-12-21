i = int(input())
s = []
star= 0
x = True
for _ in range(i):
    p = int(input())
    f = int(input())
    sum = (p*5)-(f*3)
    s.append(sum)


for i in s:
    if i > 40:
        star+=1
    else:
        x = False

if x == True:
    print(f"{star}+")
else:
    print(star)