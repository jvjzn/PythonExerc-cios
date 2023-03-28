c = 1

while not c == 11:
    print(c, end=' ')
    c += 1

print('-'*12)

n = 1

par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Impares: {}\nPares: {}'.format(impar,par))