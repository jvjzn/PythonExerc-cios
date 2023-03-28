from random import sample

n = list()

qnt = int(input('Quantos jogos deseja sortear?\n>>> '))
cont = 0
while cont < qnt:
    n.append(list(sample(range(1,60),6)))
    print(f'Jogo {cont+1}: {n[cont]}')
    cont += 1
