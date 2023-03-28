n1 = float(input('Insira a primeira nota>'))
n2 = float(input('Insira a segunda nota>'))

if (n1+n2)/2 < 5:
    print('Reprovado.')
elif (n1+n2)/2 > 5 and (n1+n2)/2 < 7:
    print('Recuperação.')
else:
    print('Aprovado.')
