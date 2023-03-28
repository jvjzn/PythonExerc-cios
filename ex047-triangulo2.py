a = float(input('Insira o comprimento da primeira reta> '))
b = float(input('Insira o comprimento da segunda reta> '))
c = float(input('Insira o comprimento da terceira reta> '))



if a + b > c and a + c > b and c + b > a:
    print('As retas são capazes de formar um triângulo. ')
    if a == b == c:
        print('Será formado um triângulo equilátero.')
    elif a != b != c != a:
        print('Será formado um triângulo escaleno.')
    else:
        print('Será formado um triângulo isósceles.')
else:
    print('As retas não são capazes de formar um triângulo.')