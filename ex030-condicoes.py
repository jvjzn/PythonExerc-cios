nome = str(input('Insira seu nome: ')).strip()
if nome == 'Joao':
    print('Esse é um nome muito comum.')
print('Nome: {}'.format(nome))

n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))
print ('A sua média foi: {:.2f}.\n'.format((n1+n2)/2)+'Parabéns.' if n1+n2/2>=6 else 'Abaixo do mínimo.')