chico = int(input("Digite a altura de Chico em centímetros: "))
ze = int(input("Digite a altura de Zé em centímetros: "))
tc=2
tz=3
ano=0
while ze <= chico:
    ze = ze+tz
    chico = chico + tc
    ano+=1
    print(chico, "", ze, "", ano)