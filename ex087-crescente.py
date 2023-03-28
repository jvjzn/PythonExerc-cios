lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso!')
        while True:
            decisao = int(input('Deseja encerrar lista?[1]Sim [2]Não\n>>'))
            if decisao == 1 or decisao == 2:
                break
            else:
                print('Opção inválida.')
    else:
        print('Este número já está na lista! Tente outro.')
    
    if decisao == 1:
        break

lista.sort()
print(f'Lista formada em ordem crescente: {lista}')