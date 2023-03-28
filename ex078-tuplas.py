#tuplas são imutáveis

lanche = 'pizza', 'hamburguer', 'batata', 'leite'

#for cont in range(0, len(lanche)):
#    print(f'vou comer {len[cont]} na posição {cont}')

# ou

for pos, comida in enumerate(lanche):
    print(f'vou comer {comida} na posição {pos}.')

print('-'*12)

print(sorted(lanche))

print('-'*12)

a = (4, 3, 1)
b = (5, 7, 2, 9)
c = b + a
print(c)
print(c.index(5))

print('-'*12)

pessoa = ('Jotinha', 19, 'M', 52.5)
#del(pessoa)
print(pessoa)