nome = str(input('Nome> '))

if nome == 'Joao':
    print ('Nome pelas ein carinha')

elif nome == 'Gus' or nome == 'Gustavinho' or nome == 'Gordin':
    print ('Suspeito...')

elif nome in 'Sama Cleiton Cleiders Zicleiders':
    print ('Por favor, evada este indivíduo do local.')

else:
    print ('Oi, {}.'.format(nome))

print('Tenha um bom dia.')
