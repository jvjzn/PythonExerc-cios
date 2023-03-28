lista = list()
dado = list()

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    decisao = str(input('Deseja continuar? [S/N]\n>>'))
    if decisao in 'Nn':
        break

print('-'*30)

print(f'Foram cadastradas {len(lista)} pessoas.')

mai = men = 0
nomeMa = list()
nomeMe = list()

for c in range (len(lista)):
    if c == 0:
        mai = men = lista[c][1]
    else:
        if lista[c][1] <= men:
            men = lista[c][1]

        if lista[c][1] >= mai:
            mai = lista[c][1]

for i in range (len(lista)):
    if lista[i][1] == mai:
        nomeMa.append(lista[i][0])
    if lista[i][1] == men:
        nomeMe.append(lista[i][0])

print(f'O maior peso foi {mai}. De {nomeMa} ')
print(f'O menor peso foi {men}. De {nomeMe} ')
