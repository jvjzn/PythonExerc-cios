ma, me, num, s, q, p = 0, 0, 0, 0, 0, 0

while p != 2:
    num = int(input('Insira um número: '))
    
    if q<1:
        ma = me = num
    elif num > ma:
        ma = num
    elif num < me:
        me = num
    
    s += num
    q += 1

    p = int(input('Deseja continuar? [1]Sim [2]Não\n>>> '))

print("A média entre todos os valores: {:.2f}\nMaior número: {}\nMenor número: {}".format(s/q,ma,me))
