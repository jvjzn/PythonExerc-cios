nome = str(input('Insira nome completo: '))

print('Todas as letras maiúsculas> {}'.format(nome.upper()))
print('Todas as letras minúsculas> {}'.format(nome.lower()))

print('Quantidade de letras> {}'.format(len(nome.replace(' ',''))))

d = nome.split()
print('Quantidade de letras 1º nome> {}'.format(len(d[0])))
