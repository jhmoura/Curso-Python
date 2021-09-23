carlos = float(input("Digite o salário do Carlos: "))
joao = carlos/3

rp = carlos
rf = joao
mes=0
while rp > rf:
    rp = rp+rp*0.02
    rf = rf+rf*0.05
    mes+=1
    print(rp, "", rf, "", mes)