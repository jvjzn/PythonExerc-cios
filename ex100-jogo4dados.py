from random import randint

from operator import itemgetter

jogadores = {'jogador1' : randint(1,6), 'jogador2' : randint(1,6), 'jogador3' : randint(1,6), 'jogador4' : randint(1,6)}


for k,v in jogadores.items():
    print(f'O {k} tirou o número: {v}')


ranking = list()

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)


print("Ranking: ")

i = 0

for i,v in enumerate(ranking):
    print(f'{i}º lugar: {v[0]} com {v[1]}')
