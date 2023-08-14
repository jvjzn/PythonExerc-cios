pessoas = {'nome': 'Jotinha', 'sexo': 'M', 'idade': 19}

print(pessoas['nome'])

print(30*'-=')

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(30*'-=')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print(30*'-=')

for k, v in pessoas.items():
    print(f'{k} = {v}')

print(30*'-=')

del pessoas['sexo']
pessoas['nome'] = 'Crocodilo'
pessoas['peso'] = 300.2

for k, v in pessoas.items():
    print(f'{k} = {v}')

print(30*'-=')

estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}

brasil = []

brasil.append(estado1)
brasil.append(estado2)

print(brasil)

print(30*"-=")

aluno = dict()

aluno['nome'] = 'jotola'
aluno['idade'] = 20

print(aluno)