num = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito,','dezenove','vinte'

while True:
    entrada = int(input('Insira um número entre 0 e 20: '))
    if 0> entrada >20:
        print('Tente novamente. ', end='')
        continue
    else:
        print(f'{entrada} por extenso é {num[entrada]}.') 
        while True:
            resp = int(input('Deseja escolher outro número? [1]SIM [2]NÃO\n>>'))
            if resp == 2 or resp == 1:
                break
            else:
                print('Tente novamente. ', end='')
                continue
    if resp == 2:
        print('- Programa finalizado. -')
        break
