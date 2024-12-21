x = int(input())
z = []
seen = set()
a =0
for _ in range(x):
    y = int(input())
    z.append(y)
    if not y in seen:
        seen.add(y)

y = sorted(seen, reverse=True)

for i in z:
    if i == y[2]:
        a += 1
print(f"{y[2]} {a}")