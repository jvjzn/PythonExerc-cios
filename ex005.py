nome = str(input('Insira seu nome: '))
print ('Vamos fazer contas {:-^16}!' .format(nome))

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

print ('-'*5)

print('A soma é {}. \nA multiplicação é {}. \nA divisão é {:.2f}'.format(n1+n2,n1*n2,n1/n2))
print('A divisão inteira é {}, a potenciação é {}.' .format(n1//n2,n1**n2), end=' ')
print('O resto da divisão é {}.' .format(n1%n2))

print ('-'*5)