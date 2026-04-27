valor = int(input("Escolha o valor inicial: "))
fatorial = 1
for f in range(valor, 0, -1):
    fatorial *= f
print(fatorial)