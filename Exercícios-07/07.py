vetor1 = []
for num in range(10):
    vetor1.append(int(input(f"Digite o número da posição {num+1}: ")))

print(vetor1)
print(f"O maior elemento da lista é {max(vetor1)} e se encontra na posição {vetor1.index(max(vetor1))}")