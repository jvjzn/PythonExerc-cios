#import math
#usar math.comando()
from math import sqrt,ceil,floor
num = int(input('Insira um número: '))
print ('A raiz quadrada: {:.2f}'.format(sqrt(num)))
num2 = float(input('Digite um número com decimais: '))
print ('Arredondamento para cima: {}\n Arredondamento para baixo: {}'.format(ceil(num2),floor(num2)))

