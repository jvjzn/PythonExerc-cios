from random import randint
from time import sleep

n1 = randint(0,5)

print('O computador pensou em um número de 0 a 5.')
n2 = int(input('Adivinhe qual é o número: '))
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)

if n2 == n1:
    print('Você acertou! {}'.format(n1))
else:
    print('Errou. Resposta: {}'.format(n1))