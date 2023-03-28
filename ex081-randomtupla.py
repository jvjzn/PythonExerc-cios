from random import sample

n = tuple(sample(range(10),5))

print(f'Os números sorteados foram: {n}')
print('-'*12)

print(f'O maior valor {max(n)}')
print(f'O menor valor {min(n)}')