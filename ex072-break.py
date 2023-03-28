q, n, s = 0, 0, 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        print(f'A soma dos números: {s}\n{q} números foram digitados')
        break
    s += n
    q += 1
