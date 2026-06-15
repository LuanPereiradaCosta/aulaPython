cont = 0
while True:
    n = int(input("Digite um número: "))
    if 100 <= n <= 200:
        cont +=1
    if n == 0:
        break
print(f"Foram digitados entre 100 e 200: {cont}")