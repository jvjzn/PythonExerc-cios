
idadeH = 0
nome = 0
ti = 0
idadeM = 0

for c in range (0,4):
    s1 = int(input('Insira o sexo ([1]masculino [2]feminino) : '))
    if s1 == 1:
        n = str(input('Insira o nome: '))
        i = int(input('Insira a idade: '))
        if i > idadeH:
            idadeH = i
            nome = n
        ti += i
    elif s1 == 2:
        n = str(input('Insira o nome: '))
        i = int(input('Insira a idade: '))
        if i < 20:
            idadeM += 1
        ti += i
        
print('A média de idade do grupo: {}\nO nome do homem mais velho: {}\nQuantidade de mulheres com menos de 20 anos: {}'.format(ti/4,nome,idadeM))
