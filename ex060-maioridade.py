from datetime import date

anoatual = date.today().year

m = 0

for c in range(0,7):
    n = int(input('A data de nascimento: '))
    if anoatual-n >=18:
        m += 1

print('{} pessoas atingiram a maioridade, {} ainda não.'.format(m,7-m))
