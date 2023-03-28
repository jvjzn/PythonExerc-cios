from random import randint

op = int(input('Escolha:\n[1]Pedra\n[2]Papel\n[3]Tesoura\n>>>'))

c = randint(1,3)

if (op == 1 and c == 1) or (op == 2 and c == 2) or (op == 3 and c == 3):
    print('Empate.')
elif op == 1 and c == 2:
    print('Você perdeu. Computador escolheu papel.')
elif op == 1 and c == 3:
    print('Você ganhou! Computador escolheu tesoura.')
elif op == 2 and c == 1:
    print('Você ganhou! Computador escolheu pedra.')
elif op == 2 and c == 3:
    print('Você perdeu. O computador escolheu tesoura.')
elif op == 3 and c == 1:
    print('Você perdeu. Computador escolheu pedra.')
elif op == 3 and c == 2:
    print('Você ganhou! O computador escolheu papel.')
else:
    print('Opção inválida.')
