from datetime import date

anoatual = date.today().year

ano = int(input('Insira o ano de nascimento> '))

if anoatual-ano < 18:
    print('Ainda não é necessário o alistamento. Faltam {} ano(os).'.format(18-(anoatual-ano)))
elif anoatual-ano == 18:
    print('Está na hora de alistar!')
else:
    print('Já passou do tempo do alistamento. Deveria ter se alistado à {} ano(os) atrás.'.format((anoatual-ano)-18))
