vt1 = []
vt2 = []
for num in range(10):
    vt1.append(int(input(f"Digite o número de posiçao {num+1}: ")))

print(vt1)
for num2 in range(len(vt1)):
    vt2.append((vt1[num2]**2))

print(vt1)
print(vt2)