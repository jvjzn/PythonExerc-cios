from math import hypot

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

print('O valor da hipotenusa: {:.2f}'.format(hypot(co,ca)))