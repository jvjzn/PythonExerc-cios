maiorI = 0
Qhomem = 0
Mvinte = 0

while True:

    sexo = int(input('Insira o sexo [1]M [2]F: '))

    if sexo == 1:
        Qhomem += 1

    idade = int(input('Insira idade: '))

    if idade > 18:
        maiorI += 1

    if sexo == 2 and idade < 20:
        Mvinte += 1

    continuar = int(input('Deseja continuar? [1]Sim [2]Não\n>>> '))

    if continuar == 2:
        break

print(f'A){maiorI} pessoas tem mais de 18 anos.\nB){Qhomem} homens foram cadastrados.\nC){Mvinte} mulheres tem menos de 20 anos.')
