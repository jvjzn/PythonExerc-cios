from math import radians,sin,cos,tan

a = float(input('Insira um ângulo:'))

print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(radians(a)),cos(radians(a)),tan(radians(a))))