lista1 = []

while True:
    lista1.append(int(input('Digite um número: ')))
    decisao = int(input('Deseja Continuar? [S/N]\n>>'))
    if decisao in 'Nn':
        break

listaP = []
listaI = []

for c in lista1:
    if (c % 2) == 0:
        listaP.append(c)
    else:
        listaI.append(c)

print('-'*20)

print(f'lista inicial: {lista1}')
print(f'Apenas pares: {listaP}')
print(f'Apenas ímpares: {listaI}')