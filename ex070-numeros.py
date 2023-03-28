num = 0
total = 0
q = 0

print('Digite 999 para interromper o programa.')
while num != 999:
    num = int(input('Insira um número: '))
    if num !=999:
        q += 1
        total += num

print('A soma total: {}\n{} números foram inseridos.'.format(total,q))