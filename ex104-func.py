def lin():
    print(10*'-=')

def titulo(msg):
    lin()
    print(msg)
    lin()

#Programa Principal
titulo("Soma")

#-=-=-

def soma(a,b):
    r = a + b
    print(r)

soma(17,124)


titulo("Multiplicação")

def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números.", end='')
    print('FIM')

contador(3,6,9)

titulo("Dobrar")

def dobra(lista):
    for v in range(0, len(lista)):
        print(f" {lista[v]*2} ", end='')

valores = [1,4,7,23]

dobra(valores)