r = ""

pessoas = []

while r != 'N':
    nome = str(input("Nome: "))
    sexo = str(input("Sexo(M/F): ")).upper()[0]
    idade = int(input("Idade: "))

    pessoaAux = {'nome' : nome, 'sexo' : sexo, 'idade' : idade}
    pessoas.append(pessoaAux)

    r = str(input("Quer continuar?(S/N) >> ")).upper()[0]
    
qntPessoas = len(pessoas)

print(f"O grupo tem {qntPessoas} pessoas.")

mediaIdade = 0

for i in range(0,len(pessoas)):
    mediaIdade += (pessoas[i]['idade'])

print(30*"-=")

mediaIdade = mediaIdade/qntPessoas

print(f"A média de idade é {mediaIdade} anos.")

mulheres = []

for i in range (0,len(pessoas)):
    if pessoas[i]['sexo'] == 'F':
        mulheres.append(pessoas[i]['nome'])

print(f"As mulheres cadastradas foram: {mulheres}")

acimaMedia = []

for i in range (0,len(pessoas)):
    if pessoas[i]['idade'] > mediaIdade:
        acimaMedia.append(pessoas[i]['nome'])

print(f"lista das pessoas que estão acima da média: {acimaMedia}")