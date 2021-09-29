v1 = []
for i in range(8):
    v1.append(int(input("Digite um número: ")))
n1 = int(input("Agora digite um número entre 0 e 7: "))
n2 = int(input("Agora digite mais um número entre 0 e 7: "))

soma = v1[n1]+v1[n2]
print(f"A soma entre as duas posições da lista é de {soma}")