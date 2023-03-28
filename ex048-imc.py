p = float(input('Insira o peso em kg> '))
a = float(input('Insira a altura em metros>'))

if p/(a**2) < 18.5:
    print('Abaixo do peso.')
elif p/(a**2) >= 18.5 and p/(a**2) < 25:
    print('Peso ideal.')
elif p/(a**2) >= 25 and p/(a**2) < 30:
    print('Sobrepeso.')
elif p/(a**2) >= 30 and p/(a**2) <= 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
