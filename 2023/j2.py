x = int(input())
y = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}
sum = 0
for _ in range(x):
    z  = input()
    sum +=  y[z]
    
print(sum)