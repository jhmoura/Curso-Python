co = int(input("Quantos números você vai digitar: "))
ma = 0
for i in range(co):
    num = int(input("Digite um número: "))
    if num > ma:
        ma = num
    else:
        pass
print(ma)