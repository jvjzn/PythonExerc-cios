lista = []

while True:
    lista.append(int(input('Insira um valor: ')))
    decisao = int(input('Deseja continuar?[1]Sim [2]Não\n>>'))
    if decisao == 2:
        break

print('-'*20)

print(f'A) Foram digitados: {len(lista)} valores')
lista.sort(reverse=True)
print(f'B) Lista em ordem decrescente: {lista}')

if 5 in lista:
    print('C) O valor 5 está na lista.')
else:
    print('C) O valor 5 NÃO está na lista.')
