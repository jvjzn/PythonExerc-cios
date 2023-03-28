num = int (input('Insira o primeiro número: '))

ma = num
me = num

num = int (input('Insira o segundo número: '))

if num > ma:
    ma = num
else:
    if num<ma:
        me = num

num = int (input('Insira o terceiro número: '))

if num > ma:
    ma = num
else:
    if num<ma:
        if num<me:
            me = num

print ('O maior número digitado foi: {}\nO menor número digitado foi: {}'.format(ma,me))