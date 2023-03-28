n = int(input('Insira um número: '))
res = n
n -= 1
while n != 0:
    res = res*n
    n -= 1

print('Fatorial: {}'.format(res))

#ou
'''
from math import factorial

print(factorial(5))


'''