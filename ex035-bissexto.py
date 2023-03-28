'''a = str(input('Insira um ano: '))

q = len(a)-1

b = int(a)

if a[q] == '0' and a[q-1] == '0':
    if b%400 == 0:
        c = True
    else:
        c = False
else:
    if b%4 == 0:
        c = True
    else:
        c = False

print('É um ano bissexto.' if c == True else 'Não é um ano bissexto.')'''

#ou
from datetime import date

a = int(input('Insira um ano (Insira 0 para analizar o ano atual): '))

if a == 0:
    a = date.today().year

print('{} é um ano bissexto.'.format(a) if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 else '{} Não é um ano bissexto.'.format(a))