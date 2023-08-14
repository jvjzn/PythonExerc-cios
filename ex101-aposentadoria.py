from datetime import datetime



nome = str(input("Nome: "))
anoNascimento = int(input("Ano de nascimento: "))
ctps = int(input("Carteira de Trabalho (0 não tem): "))

pessoa = {'nome':nome,'idade': datetime.now().year - anoNascimento,'ctps':ctps}

print(30*"-=")

if ctps == 0:
    for k,v in pessoa.items():
        print(f'{k} tem valor: {v}')
else:

    anoContratacao = int(input("Ano da Contratação: "))
    novosValores = {'anoContratacao' : anoContratacao,'salario' : float(input("Salário: R$")), 'aposentadoria': (anoContratacao - anoNascimento) + 35}

    pessoa.update(novosValores)

    for k,v in pessoa.items():
        print(f'{k} tem valor: {v}')
    