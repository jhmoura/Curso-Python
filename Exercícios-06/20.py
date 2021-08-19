P = True
np=0
nt=0
while P == True:
    N = int(input("Digite un número: "))
    if N == 1000:
        print("ACABOU!")
        break

    if N%2 == 0 :
        np+=1
        nt+=1
        print(f"Forma lidos {nt} números, e {np} são pares.")
    else:
        nt+=1
        print(f"Forma lidos {nt} números, e {np} são pares.")