from random import choice,shuffle

print('Insira o nome dos alunos: ')
a1 = str(input('> '))
a2 = str(input('> '))
a3 = str(input('> '))
a4 = str(input('> '))

nomes = [a1,a2,a3,a4]

print('O aluno sorteado para apagar o quadro é: {}'.format(choice(nomes)))

shuffle(nomes)

print('A ordem de apresentação de trabalhos será: {}'.format(nomes))