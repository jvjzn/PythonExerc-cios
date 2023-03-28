from datetime import date

anoatual = date.today().year

ano = int(input('Insira o ano de nascimento do atleta> '))

if anoatual-ano <= 9:
    print('Atleta mirim')
elif anoatual-ano <= 14:
    print('Atleta infantil')
elif anoatual-ano <= 19:
    print('Atleta junior')
elif anoatual-ano <= 25:
    print('Atleta sênior')
else:
    print('Atleta master')
