idade = int(input("Digite sua idade: "))
print(f"Com a idade: {idade} sua categoria sera: ")
if 0 < idade <= 4:
    print(f"Para a idade {idade} não existe a categoria")
elif 5 <= idade <= 7:
    print("Infatil A")
elif 8 <= idade <= 10:
    print("Infatil B")
elif 11 <= idade <= 13:
    print("Juveil A")
elif 14 <= idade <= 17:
    print("Juvenil B")
elif 18 <= idade:
    print("Adulto")
else:
    print("Valor de idade inválido")
