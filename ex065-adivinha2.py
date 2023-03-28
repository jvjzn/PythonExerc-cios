from random import randint

n = randint(0,10)
op = 11

while op != n:
    op = int(input('Qual número o computador pensou?\n>>>'))
    if op != n:
        print('Errou.', end=' ')
        if op < n:
            print('É maior!')
        else:
            print('É menor!')
print('Acertou! O computador pensou no {}'.format(n))