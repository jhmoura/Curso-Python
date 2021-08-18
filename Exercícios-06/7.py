n=0
x=0
while n < 10:
    n1 = int(input('Escreva um número: '))
    if n1%2 == 0:
        x+=n1
    else:
        print('Número impar!')
    n+=1
    
xr=x/10
print(f'A média é {xr}')