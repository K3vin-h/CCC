i =  input()
s = []
y = ""
num = []
for x in i:

    if x == "+":
        y = "tighten"
    elif x == "-":
        y = "loosen"
    elif x.isnumeric() == True:
        num.append(x)
    else:
        if len(num) > 0:
            print(f"{''.join(s).strip()} {y} {''.join(num).strip()}")
            y = ""
            s = []
            num = []
        s.append(x)
print(f"{''.join(s).strip()} {y} {''.join(num).strip()}")
