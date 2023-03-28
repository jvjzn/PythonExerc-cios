teste = list()
teste.append('João')
teste.append('19')
print(teste)

print('-'*20)

galera = list()
galera.append(teste[:])
print(galera)

print('-'*20)

teste[0] = 'Maria'
teste[1] = 22
print(teste)
galera.append(teste[:])
print(galera)

print('-'*20)

pessoas = [['Gus', 20], ['Sam', 19], ['Ke', 40], ['Bia', 17]]
print(pessoas)
print(pessoas[0])
print(pessoas[3][0])
print(pessoas[1][1])

print('-'*20)

galera2 = list()
dado = list()

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()

print(galera2)