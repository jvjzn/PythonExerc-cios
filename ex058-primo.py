n = int(input('Insira um número: '))

res = 0

for c in range (2,n-1):
    if n%c != 0:
        pass
    elif n%c == 0:
        res = 1
        break


if res == 1:
    print('Não é um número primo.')
else:
    print('É um número primo.')