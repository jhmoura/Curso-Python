n1 = int(input('Insira um número ímpar: '))
if n1%2!=0:
    for i in range(n1+1):
        if i%2 != 0:
            print(i)
    x=False
else:
    print('Eu disse ímpar animal!!')
