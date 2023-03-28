n = int(input('Insira um número> '))
base = int(input('Escolha a base de conversão: \n [1] Binário\n [2] Octal\n [3] Hexadecimal\n>'))

if base == 1:

    print('{} em binário: {}'.format(n,bin(n)[2:]))
elif base == 2:
    print('{} em Octal: {}'.format(n,oct(n)[2:]))
elif base == 3:
    print('{} em Hexadecimal: {}'.format(n,hex(n)[2:]))
else:
    print ('Escolha uma opção de base válida!')