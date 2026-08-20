for a in range(0, 3):
    alt = float(input("Digite a sua altura: "))

    if a == 0:
        maior = alt
        menor = alt
    else:
        if alt > maior:
            maior = alt
        if alt < menor:
            menor = alt

print(f"maior: {maior}")
print(f"menor: {menor}")
