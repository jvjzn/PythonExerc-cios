numeros = [[],[]]

for c in range(0,7):

    v = int(input('Insira um número: '))

    if v % 2 == 0:
        numeros[0].append(v)
    else:
        numeros[1].append(v)

numeros[0].sort()
numeros[1].sort()
print('Pares:' , numeros[0])
print('Impares:' , numeros[1])
