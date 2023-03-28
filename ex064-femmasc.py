op = str(input('Insira o sexo ([M]masculino [F]feminino): ')).lower()

while op != 'm' and op != 'f':
    op = str(input('Opção inválida. [M]masculino [F]feminino: '))

print('Sexo {} registrado.'.format(op.upper()))
