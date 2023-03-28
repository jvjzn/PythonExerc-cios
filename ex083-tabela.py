lista = 'manga',2.3,'maçã',1.5,'banana',2.2
print('-'*25)
print(f'{"Listagem de preços":^25}')
print('-'*25)

c = 0
while c < len(lista):
    print(f'{lista[c]:.<15}',f'R${lista[c+1]:7.2f}')
    c += 2

print('-'*25)