
q = int(input('Insira a quantidade de primeiros elementos Fibonacci deseja ver: '))

t1 = 1
t2 = 1
t3 = 1

i = 3

if q == 1:
    print(0)
elif q == 2:
    print(0,1, end=' ')
elif q == 0:
    print('')
else:
    print(0,1, end=' ')
    while i <= q:
        print(t3, end=' ')
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        i += 1