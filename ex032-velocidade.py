vel = float(input('Velocidade do carro: '))
print('Foi multado e terá que pagar R${:.2f}'.format((vel-80)*7) if vel>80 else 'Não foi multado')