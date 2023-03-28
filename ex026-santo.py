c = str(input('Insira o nome de uma cidade: ')).strip()

if c[:5].upper() == 'SANTO':
    print('O nome da cidade começa com "Santo"')
else:
    print('O nome da cidade não começa com "Santo"')
