m = int(input("insira um valor inteiro: "))
n = int(input("insira outro valor inteiro, maior que o anterior: "))


while not m > n:
    stringNum = str(m)
    tamanho = len(stringNum)
    x = 0

    while (x < tamanho):
        
        y = 1
        aux = 0

        if (m >= 10):
            while y < tamanho:
                if ( stringNum[x] == stringNum[y]):
                    aux +=1
                    break
                y += 1
                
        x += 1

        if (x == (tamanho - 1)):
            if (aux == 0):
                print(m,end=' ')

    m += 1