casas = 1
graos_na_casa = 1
total_graos = 0

while casas <= 64:
    total_graos += graos_na_casa
    graos_na_casa *= 2
    casas += 1

print(total_graos)
