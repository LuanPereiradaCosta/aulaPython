n1 = int(input("Digite um número: "))
print(f"O número: {n1} é: ", end=" ")
if n1%2 == 0:
    print("Par e", end=" ")
else:
    print("impar e", end=" ")
if n1 > 0:
    print("é positivo!")
elif n1 == 0:
    print("é neutro")
else:
    print("é negativo")