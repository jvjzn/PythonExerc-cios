def lin():
    print(20*"=")

def contador(inicio,fim,passo):

    lin()

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if inicio < fim:
        for i in range(inicio,fim+1,passo):
            print(f"{i} ",end='')
            i+= passo
    else:
        for i in range(inicio,fim-1,-passo):
            print(f"{i} ",end='')
            i+= passo

    print("")
    lin()


print("Teste 1")
contador(1,10,1)

print("Teste 2")
contador(10,0,2)

print("Sua vez!")

contador(int(input("Digite o número inicial: ")),int(input("Digite o número final: ")),int(input("Digite os passos: ")))