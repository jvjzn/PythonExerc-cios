num = [2,5,9,1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Lista com {len(num)} elementos.')
num.insert(2,4)
print(num)
num.pop(0)
print(num)
num.remove(4)
print(num)

print('-'*20)

for c, v in enumerate(num):
    print(f'Pos. {c} -> valor {v} ')

print('-'*20)
'''
num2 = []

for cont in range (0,5):
    num2.append(int(input('Digite um valor: ')))
print(num2)
'''
print('-'*20)

a = [2,3,4,7]
b = a
print('A ',a)
print('B ',b)
b[2] = 8
print('A ',a)
print('B ',b)

print('-'*20)

c = a[:]
c[1] = 9
print('A ',b)
print('C ',c)
