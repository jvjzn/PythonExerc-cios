frase = str(input('Insira uma frase qualquer\n>>> ')).strip().lower()
frase = frase.replace(' ','')

res = 0
b = len(frase)-1

for c in range (0,len(frase)):
    if frase[c] != frase[b]:
        print('Não é palíndromo.')
        res = 1
        break
    elif c == b:
        break
    else:
        b -= 1
        
if res == 0:
    print('É um palíndromo.')
    