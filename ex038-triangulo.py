a = float(input('Insira o comprimento da primeira reta> '))
b = float(input('Insira o comprimento da segunda reta> '))
c = float(input('Insira o comprimento da terceira reta> '))

if a + b > c and a + c > b and c + b > a:
    print('As retas são capazes de formar um triângulo. ')
else:
    print('As retas não são capazes de formar um triângulo.')