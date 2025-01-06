S = input()
T = input()
temp = ""
x = False
for i in range(len(T)):
   temp = T[i:] + T[:i] 
   if temp in S:
        x = True
        break
if x == True:
    print("yes")
else:
    print("no")