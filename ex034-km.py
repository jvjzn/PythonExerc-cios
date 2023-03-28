km = float(input('Insira a distância da viagem em Km> '))
print('O preço da passagem: R${:.2f}' .format(km*0.5) if km<=200 else 'O preço da passagem: R${:.2f}' . format(km*0.45))