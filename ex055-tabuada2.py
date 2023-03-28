n = int(input('Escolha um número: '))

for c in range(1,11):
    print('{:2} x {} = {:2}'.format(c,n,c*n))