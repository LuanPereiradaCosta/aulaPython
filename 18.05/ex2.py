qNum = int(input("Quantidas a serem lidos"))
faixa1 = faixa2 = faixa3 = faixa4 = 0
while qNum > 0:
    num = int(input("Informe o número: "))
    if num < 0 or num > 100:
        print("Número invalido")
        continue
    elif 0 <= num <= 25:
        faixa1 += 1
    elif 26<= num <= 50:
        faixa2 += 1
    elif 51<= num <= 76:
        faixa3 += 1
    elif 77<= num <= 100:
        faixa4 += 1
    qNum -= 1
print(f"Quantidade faixa 1: {faixa1}")
print(f"Quantidade faixa 2: {faixa2}")
print(f"Quantidade faixa 3: {faixa3}")
print(f"Quantidade faixa 4: {faixa4}")