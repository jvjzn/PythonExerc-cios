from random import randint
vc = 0

while True:

    comp = randint(0,10)
    
    pi = int(input('Par ou ímpar? [1]Par [2]Ímpar\n>>> '))
    op = int(input('Jogue: '))

    if (pi == 1 and (op+comp) % 2 == 0) or (pi == 2 and (op+comp) % 2 != 0):
        print(f'Você ganhou! Computador escolheu: {comp}')
        vc += 1
    else:
        print(f'Você perdeu. Computador escolheu {comp}\nVitórias: {vc}')
        break
