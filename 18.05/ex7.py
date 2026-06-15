maior = 0
while True:
    num = int(input("Digite um número: "))
    if maior == 0:
        maior = num
    elif maior < num:
        maior = num
    if num == -1:
        break
print(maior)
