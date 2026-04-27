cont = 0
for n in range(0,6):
    num = int(input("Digite números: "))
    if num < 0:
        cont +=1
print(f"Tem {cont} Negativos.")