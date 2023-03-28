for c in range(1,6):
    print (c)
print ('----')
for c in range(7,0,-1):
    print (c)
print ('----')
for c in range(0,10,2):
    print (c)
print ('----')

i = int(input('Início: '))
f = int(input('Fim:'))
p = int(input('Passo: '))

for c in range(i, f, p):
    print (c)
print('--FIM--')