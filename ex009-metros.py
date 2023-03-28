import cmath


m = float(input('Insira um valor em metros: '))
print('Convertendo para kilômetros: {}km\nConvertendo para hectômetros: {}hm\nConvertendo para decâmetros: {}dam' .format(m/1000,m/100,m/10))
print('Convertendo para decímetros: {}dm\nConvertendo para centímetros: {}cm\nConvertendo para milímetros: {}mm' .format(m*10,m*100,m*1000))
