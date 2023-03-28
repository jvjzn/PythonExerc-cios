from time import sleep

op = 0

while op != 5:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    while op !=5:
        print('-'*12)
        op = int(input('-Escolha um tipo de operação:\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\n>>> '))
        if op == 1:
            print('A soma: {} + {} = {}'.format(n1,n2,n1+n2))
            sleep(3)
        if op == 2:
            print('A multiplicação: {} * {} = {}'.format(n1,n2,n1*n2))
            sleep(3)
        if op == 3:
            if n1>n2:
                print('O maior: {}'.format(n1))
                sleep(3)
            elif n1<n2:
                print('O maior: {}'.format(n2))
                sleep(3)
            else:
                print('Os dois números são iguais.')
                sleep(3)
        if op == 4:
            break
        if op == 5:
            break

print('-'*12)
print('Programa finalizado.')