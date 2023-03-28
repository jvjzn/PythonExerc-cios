num = 0
while True:
    num = int(input('Insira um número para ver sua tabuada (-1 para finalizar): '))
    if num == -1:
        break
    for c in range (1,11):
        print(f'{num} x {c:2} = {num*c:2}')
print('Programa finalizado.')
