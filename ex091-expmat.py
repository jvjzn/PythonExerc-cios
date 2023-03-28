expressao = []

expressao = str(input('Digite uma expressão: '))

contador = 0

for c in expressao:
    if c == '(':
        contador += 1
    elif c == ')':
        contador -= 1
    if contador < 0:
        break

if contador == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')