from random import randint

segredo = randint(000,999)
segredoString = str(segredo).zfill(3)
chute = 1000
cont = 0
acertou = 0

while (chute != segredo) and (cont < 6):
  
  chute = int(input("Qual número o programa pensou? (Número de até 3 digitos, >= 0)\n>>>"))


  if chute == segredo:
    acertou = 1
  
  else:
    x = 0
    digito = 0
  
    while x < 3:
        if (str(chute).zfill(3).count(segredoString[x]) > 0):
            digito += 1
  
        x +=1

  
    y = 0
    posicao = str(chute).zfill(3)
    posicoes = 0

    while y < 3:
        if (posicao[y] == segredoString[y]):
            posicoes +=1

        y +=1


    print(f"{posicoes} posições certas / {digito} digitos casados")
    
    cont += 1

if acertou > 0:
  print(f"Parabéns, Você adivinhou o número {segredo}!")

else:
  print(f"Você não adivinhou o número {segredo}.")