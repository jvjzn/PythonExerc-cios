nomeJogador = str(input("Insira o nome do jogador: "))

qntPartidas = int(input(f"Insira a quantidade de partidas jogadas por {nomeJogador}: "))

partidas = list()

for i in range(0,qntPartidas):

    partidas.append(int(input(f"Quantos gols {nomeJogador} fez na partida {i+1}? >> ")))


aproveitamento = {'nome' : nomeJogador, 'golsEmPartidas' : partidas, 'totalGols':sum(partidas)}


print(30*"-=")


for k,i in aproveitamento.items():

    print(f'{k} tem valor {i}')


print(30*"-=")


for k,v in enumerate(aproveitamento['golsEmPartidas']):
    print(f" Na partida {k+1}, fez {v} gols.")