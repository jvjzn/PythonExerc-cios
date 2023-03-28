p = float(input('Insira o preço normal do produto> '))
c = float(input('Insira a condição de pagamento:\n[1]À vista(dinheiro/cheque)\n[2]À vista no cartão\n[3]Em até 2x no cartão\n[4]3x ou mais no cartão\n>>>'))

if c == 1:
    print('10% de desconto.\nNovo valor: R${:.2f}'.format(p-(0.1*p)))
elif c == 2:
    print('5% de desconto.\nNovo valor: R${:.2f}'.format(p-(0.05*p)))
elif c == 3:
    print('Preço normal: R${:.2f}'.format(p))
elif c == 4:
    print('20% de juros.\nNovo valor: R${:.2f}'.format(p+(0.2*p)))
else:
    print('Opção inválida!')
