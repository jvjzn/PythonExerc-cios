tpreco = 0
qproduto = 0
mp = 0
mn = ''
i = 0

while True:

    nome = str(input('Insira o nome do produto: '))

    preco = float(input('Insira o preço do produto: '))

    if i != 1:
        mp = preco
        mn = nome
        i += 1

    if preco < mp:
        mp = preco
        mn = nome

    tpreco += preco

    if preco > 1000:
        qproduto += 1

    x = int(input('Deseja finalizar o programa? [1]Sim [2]Não\n>>> '))

    if x == 1:
        break

print(f'A)R${tpreco:.2f} foi o total gasto.\nB){qproduto} produtos custam mais de R$1.000,00.\nC){mn} é o produto mais barato.')