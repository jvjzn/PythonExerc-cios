num = str(input('Insira um número entre 0 e 9999: '))
casas = ['unidade','dezena','centena','milhar']

x = 0
y = len(num)-1

while y>=0:
    print ('{}: {}'.format(casas[x],num[y]))
    y -= 1
    x += 1
