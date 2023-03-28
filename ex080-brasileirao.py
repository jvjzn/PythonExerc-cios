times = 'Palmeiras','Corinthians','Fluminense',	'Athletico-PR','Flamengo', 'Internacional',	'Atlético-MG', 'Bragantino', 'Santos', 'São Paulo',	'Goiás', 'Botafogo','América-MG', 'Ceará', 'Coritiba', 'Avaí', 'Cuiabá', 'Fortaleza', 'Atlético Goianiense', 'Juventude'

print('A) Os 5 primeiros colocados:')
print(times[:5])
print('')
print('B) Os útimos 4 colocados da tabela:')
print(times[-4:])
print('')
print('C) Os times em ordem alfabética:')
print(sorted(times))
print('')
print(f'O Botafogo está na {times.index("Botafogo")+1}º posição')
print('')
