#Code does not work


# x = input()
# y = input()
# a = []
# b = []
# silly = None
# correct= None
# quiet = "-"
# unk = 0 
# c = 0
# bool = True
# d = set()
# for i in x:
#     a.append(i)
# for i in y:
#     b.append(i)
# if (len(a) != len(b)):
#     length = len(a) - len(b)
#     for i in range(length):
#         b.append("-")
#     bool = False

# for i in range(len(x)):
#     if b[i] == "-" and quiet == "-":
#         quiet = a[i]
#     elif a[i] != b[i]:
#         if(bool == True):
#             silly = b[i]
#             correct = a[i]
#         else:
#             unk = int(i)
#             if not a[unk] in d:
#                 d.add(a[unk])
#             else:
#                 break
#             unk = int(i) +1
#             for i in range(len(x)):
#                 if (a[unk] == b[i]):
#                     c = int(i) 
#                     break
#             silly = b[c-1]
#             correct = a[unk-1]

    
# print(f"{correct} {silly}")
# print(f"{quiet}") 
 
x = input()
y = input()
silly = None
correct= None
quiet = "-"
a = 0
b= 0
c = 0
var = False
test1 = None
test2 = None
while a < len(x) and b < len(y):
    if x[a] == y[b]:
        a += 1
        b += 1
    else:
        for i in range(len(y)):
            if y[b] == x[i]:
                c = i
                break
        if c-a >= 1:
            quiet = x[a]
            a += c
            b += 1
        else:
            # print(f"{x[a]} {y[b]}")
            # if silly == None:
            #     test1 = y[b]
            #     test2 = x[a]
            # if test1 == y[b] and test2 == x[a]:
            #     var= True
            #     silly = y[b]
            #     correct = x[a]
            a += 1
            b += 1
e =0
if a < len(x):
    for i  in range(a, len(x)):
        for j in range(len(y)):
            if x[i] != y[j] and var == True:
                quiet = x[i]
                break
            elif x[i] == y[j]:
                continue
            else:
                silly = y[j]
                correct = x[i]
                e = i
                break   
        silly = y[e]

print()

print(f"{correct} {silly}")
print(f"{quiet}")

