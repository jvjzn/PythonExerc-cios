from random import randint

def sorteia(numeros):
    i = 0
    while i != 5:
        n = randint(1,10)
        numeros.append(n)
        i += 1
    print(numeros)

def par(numeros):
    numerosPares = []
    
    for n in range(0,5):
        if numeros[n] % 2 == 0:
            numerosPares.append(numeros[n])            
    
    soma = sum(numerosPares,0)
    print(soma)


numeros = []
sorteia(numeros)

numerosPares = []
par(numeros)
