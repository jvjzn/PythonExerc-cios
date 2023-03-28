x = int(input('Insira o primeiro termo da P.A.> '))
r = int(input('Insira a razão> '))
i = 0

while i != 10:
    print(x, end=' ')
    x = x+r
    i += 1

p = int(input('\nDigite a quantidade a mais de termos que desejar ver (Digite 0 para finalizar programa): '))

if p != 0:
    i = 0
    while i != p:
        print(x, end=' ')
        x = x+r
        i += 1
else:
    print('Fim do programa.')