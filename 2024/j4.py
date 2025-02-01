A = input()
B = input()
A1 = A
silly = None
wrong = None
quiet = None

old_silly = None
old_wrong = None

for x, y in zip(A, B):
    if x != y:
        silly = x
        wrong = y
        break

SetA = set(A)
SetB = set(B)

q = SetA - SetB
print(q)
if q:
    if len(q) == 1 and silly != q.pop():
        quiet = q.pop()
    else:
        for x, y in zip(A, B):
            if x == silly and y != wrong:
                old_silly = silly
                old_wrong = wrong
                silly = None
                wrong = None
                break
        for i in q:
            if old_silly == None:
                if i != silly:
                    quiet = i
                    break
            else:
                quiet = old_silly
                break
        Alist = []
        if silly == None:
            for i in A:
                if i != quiet:
                    Alist.append(i)
            A = "".join(Alist)
            print(A)
            for x, y in zip(A, B):
                if x != y:
                    silly = x
                    wrong = y
                    break

print(f"{silly} {wrong}")   
if quiet == None:
    print("-")
else:
    print(quiet)
    if quiet == "z":
        print(f"A: {B}")

