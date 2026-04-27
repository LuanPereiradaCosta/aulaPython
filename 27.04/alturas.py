maior = menor = 0
for a in range(0,3):
    alt = float(input("Digite a sua altura: "))
    if menor == 0:
        menor = alt
    elif maior < alt:
        maior = alt
    elif menor > alt:
        menor = alt
print(f"maior: {maior}")
print(f"menor: {menor}")