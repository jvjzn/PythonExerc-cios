matriz = [[],[],[]]

parT = 0
col3 = 0
mai2 = 0

for i in range (0,3):
    for c in range (0,3):
        x = int(input(f'Digite um valor para posição {i,c}: '))
        matriz[i].append(x)
        if x % 2 == 0:
            parT += x

for d in range (0,3):
    col3 += matriz[d][2]

mai2 = matriz[1][0]

for e in range (1,3):
    if matriz[1][e] > mai2:
        mai2 = matriz[1][e]

print('-'*40)

for a in range (0,3):
    for b in range (0,3):
        print(f'[ {matriz[a][b]} ]',end="")
        if b == 2:
            print('\n',end="")

print(f'A soma dos valores pares é {parT}')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {mai2}')
