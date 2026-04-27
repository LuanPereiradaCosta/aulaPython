comeca = int(input("Digite o começo"))
acaba = int(input("Digite o final"))
contP = contI = 0
for s in range(comeca,acaba,):
    if s%2 == 0:
        contP +=s
    elif s%2 == 1:
        contI +=s
print(f"Impar {contI}")
print(f"Par {contP}")