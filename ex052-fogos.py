from time import sleep

op = int(input('Digite [1] para ligar a contagem regressiva!!! '))
if op == 1:
    for c in range(10,0,-1):
        print(c)
        sleep(1)
    print('BOOM!!!')
else:
    print ('Opção inválida.')