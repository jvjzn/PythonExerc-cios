km = float(input('Quantos Km foram percorridos durante o aluguel?\n>'))
d = float(input('Por quantos dias o carro foi alugado?\n>'))

print('O preço a ser pago é: R${:.2f}'.format(km*0.15+d*60))