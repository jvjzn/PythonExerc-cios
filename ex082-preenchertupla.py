a = (int(input('Insira o primeiro número>> ')), int(input('Insira o segundo número>> ')), int(input('Insira o terceiro número>> ')), int(input('Insira o quarto número>> ')))
print('----')
if (9 in a) == True:
    print(f'A) O 9 apareceu {a.count(9)} vezes na tupla.')
elif 9 not in a:
    print('A) O 9 não apareceu na tupla.')
if (3 in a) == True:
    print(f'B) O 3 apareceu na {a.index(3)+1}º posição primeiramente.')
elif 3 not in a:
    print('A) O 9 não apareceu na tupla.')

print('Os valores pares digitados são: ',end='')
for e in a:
    if e % 2 == 0:
        print(e, end=' ')