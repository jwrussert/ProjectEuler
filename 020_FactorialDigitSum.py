x = 1

for j in range(2, 100):
    x = x*j
    
x = str(x)
total = 0

for i in x:
    total = total + int(i)

print(total)
