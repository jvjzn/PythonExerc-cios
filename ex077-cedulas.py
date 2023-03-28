txt = 'CAIXA'
txt = txt.center(25)
print('-='*12 + '-' + '\n' + txt + '\n' + '-='*12 + '-')

valor = int(input('Insira o valor a ser sacado: '))
cedulas = [50,20,10,1]

i = 0
while valor != 0:

    res = valor // cedulas[i]
    print(f'{res} notas de R${cedulas[i]},00')
    valor = valor - (res*cedulas[i])
    i += 1
    
    
    '''res = valor // 20
    print(f'{res} notas de R$20,00')
    valor = valor - (res*20)
    res = valor // 10
    print(f'{res} notas de R$10,00')
    valor = valor - (res*10)
    res = valor // 1
    print(f'{res} notas de R$1,00')'''