frase = str(input('Insira uma frase> ')).strip()


print('Aparecem {} vezes a letra "a" nesta frase, tendo a posição {} como primeira aparição e {} como última.'.format(frase.lower().count('a'),frase.lower().find('a')+1,frase.lower().rfind('a')+1))
