tupla = 'descer', 'subir', 'Brasil', 'roda', 'ultra', 'dois'

print('VOGAIS')

for c in tupla:
    
    print(f'\nNa palavra "{c}" temos: ',end='')
    for letra in c:
        if letra in 'aeiou':
            print(letra,end=' ')
