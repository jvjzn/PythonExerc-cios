nome = str(input("Insira o nome do aluno>> "))
media = float(input("Insira a média do aluno>> "))

if media < 7:
    resultado = "Reprovado"
elif media >= 7:
    resultado = "Aprovado"

aluno = {'nome' : nome, 'media' : media,'resultado': resultado}

print('-=-=-=-=-=-')

for k,v in aluno.items():
    print(f'{k} = {v}') 

print('Conclusão: ', end="")

print(f'O aluno {aluno["nome"]} tem média {aluno["media"]} e foi {aluno["resultado"]}.')

