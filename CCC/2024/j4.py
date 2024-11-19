x = input()
y = input()
a = []
b = []
silly = None
correct= None
quiet = "-"
unk = 0 
c = 0
bool = True
d = set()
for i in x:
    a.append(i)
for i in y:
    b.append(i)
if (len(a) != len(b)):
    length = len(a) - len(b)
    for i in range(length):
        b.append("-")
    bool = False

for i in range(len(x)):
    if b[i] == "-" and quiet == "-":
        quiet = a[i]
    elif a[i] != b[i]:
        if(bool == True):
            silly = b[i]
            correct = a[i]
        else:
            unk = int(i)
            if not a[unk] in d:
                d.add(a[unk])
            else:
                break
            unk = int(i) +1
            for i in range(len(x)):
                if (a[unk] == b[i]):
                    c = int(i) 
                    break
            silly = b[c-1]
            correct = a[unk-1]

    
print(f"{correct} {silly}")
print(f"{quiet}")