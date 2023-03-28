nome = str(input('Insira o nome completo> ')).strip()

r = 'silva' in nome.lower()

if r == True:
    print('Esse nome possúi "Silva"')
else:
    print('Esse nome não possúi "Silva"')