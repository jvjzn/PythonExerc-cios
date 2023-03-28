sal = float(input('Insira o salário do funcionário: '))
if sal > 1250:
    print('O salário do funcionário foi aumentado R${:.2f}, recebendo um novo valor de R${}.' .format(sal*0.1,sal*0.1+sal))
else:
    print('O salário do funcionário foi aumentado R${:.2f}, recebendo um novo valor de R${}.' .format(sal*0.15,sal*0.15+sal))