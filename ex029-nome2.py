nome = str(input('Insira o nome completo> ')).strip()

d = nome.split()

print('O primeiro nome: {}\nO último: {}'.format(d[0],d[len(d)-1]))
