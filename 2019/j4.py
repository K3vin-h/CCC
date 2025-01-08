top = [1, 2]
bottom = [3, 4]

x = input()
for i in x:
    if i == 'H':
       top, bottom = bottom, top
    if i == 'V':
        top[0], top[1] = top[1], top[0]
        bottom[0], bottom[1] = bottom[1], bottom[0]
print(f"{top[0]} {top[1]}\n{bottom[0]} {bottom[1]}")
