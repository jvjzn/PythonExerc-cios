def maior(valores):
    m = max(valores)
    return m

valores = []

x = ""

while x != 'N':
    val = (int(input("Insira um valor: ")))
    valores.append(val)
    x = str(input("Deseja continuar?(S/N)>> ")).upper()[0]


r = maior(valores)

print(f"O maior número do conjunto é o {r}.")
