frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[4::2])
print(frase[::2])

print('-'*12)

print(frase.count('o'))
print(frase.upper().count('o'))

print('-'*12)

frase = '    Curso em Vídeo Python     '
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','Android'))

print('-'*12)

print(frase)
frase = frase.replace('Python','Android')
print(frase)

print('-'*12)

frase = 'Curso em Vídeo Python'
print('Curso' in frase)
print('Video' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))

print('-'*12)

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])

print('-'*12)

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.""")