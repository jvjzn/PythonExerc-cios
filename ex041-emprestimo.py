valor = float(input('Insira o valor da casa> '))
sal = float(input('Insira o salário do comprador> '))
anos = float(input('Insira, em anos, o prazo do pagamento> '))

m = (valor/anos)/12

if (m*100)/sal <= 30:
    print('Prestação: R${:.2f}\nO empréstimo foi aceito.'.format(m))
else:
    print('Prestação: R${:.2f}\nEmpréstimo negado.'.format(m))
    