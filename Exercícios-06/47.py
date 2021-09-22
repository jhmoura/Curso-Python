t=True
while t == True:
    print(20*"=")
    print("Escolha uma opção")
    print(20*"-")
    print("Adição        = 1")
    print("Subtração     = 2")
    print("Multiplicação = 3")
    print("Divisão       = 4")
    print("Saída         = 5")
    o=input("")
    if o == "1":
        x1=int(input("Insira um número: "))
        x2=int(input("Insira outro número: "))
        r=x1+x2
        print(f"A soma é: {r}")
        print("")
        print("")
    elif o == "2":
        x1=int(input("Insira um número: "))
        x2=int(input("Insira outro número: "))
        r=x1-x2
        print(f"A subtração é: {r}")
        print("")
        print("")
    elif o == "3":
        x1=int(input("Insira um número: "))
        x2=int(input("Insira outro número: "))
        r=x1*x2
        print(f"A multiplicação é: {r}")
        print("")
        print("")
    elif o == "4":
        x1=int(input("Insira um número: "))
        x2=int(input("Insira outro número: "))
        r=x1/x2
        print(f"A divisão é: {r}")
        print("")
        print("")
    elif o == "5":
        break
    else:
        print("Opção não suportada")
        print("")
        print("")
        continue