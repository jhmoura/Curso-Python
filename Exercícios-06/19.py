c = True
while c == True:
    n1 = int(input("Insira um número entre 100 e 999: "))
    if (100>n1) or (n1>999):
        print("Número inválido.")
    else:
        n2=str(n1)
        for i in n2:
            print(i)
        c=False