peso = float(input('Insira o peso: '))
ma = peso
me = peso

for c in range(0,4):
    peso = float(input('Insira o peso: '))
    if peso >= ma:
        ma = peso
    if peso < ma:
        me = peso

print('O maior peso: {:.2f}Kg\nO menor peso: {:.2f}Kg' .format(ma,me))
