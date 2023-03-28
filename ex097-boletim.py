dado1 = list()
dado2 = list()
classe = list()
media = 0
cont = 0
d = 0
dec2 = 0

while True:
    dado1.append(str(input('Nome: ')))
    dado2.append(float(input('Nota 1: ')))
    dado2.append(float(input('Nota 2: ')))
    dado1.append(dado2[:])
    classe.append(dado1[:])
    dado1.clear()
    dado2.clear()

    cont += 1

    dec = str(input('Deseja continuar? [S/N]'))
    if dec in 'Nn':
        break
    
    print('-'*15)

print('-'*15,'\nBoletim\n','-'*15)
print('Nº - Nome - Média')

while d < cont:
    media = sum(classe[d][1])
    media = media/2
    print(f'{d} -- {classe[d][0]} -- {media}')
    media = 0
    d += 1

print('-'*15)

while dec2 != 999:
    dec2 = int(input('Mostrar as notas de qual aluno? (999 para interromper): '))
    if dec2 == 999:
        break
    print(f'As notas de {classe[dec2][0]} são: {classe[dec2][1]}')
