mulher1 = int(input("Digite a idade da primeira mulher: "))
mulher2 = int(input("Digite a idade da segunda mulher: "))
homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))

if mulher1 > mulher2:
    menorm = mulher2
elif mulher1 < mulher2:
    menorm = mulher1
else:
    menorm = mulher1
if homem1 > homem2:
    maiorh = homem1
elif homem1 < homem2:
    maiorh = homem2
else:
    maiorh = homem1

total1 = maiorh + menorm

print(f"a idade somada da maior idade homem e menor idade mulher: {total1}")

if mulher1 > mulher2:
    maiorm = mulher1
elif mulher1 < mulher2:
    maiorm = mulher2
else:
    maiorm = mulher1
if homem1 > homem2:
    menorh = homem2
elif homem1 < homem2:
    menorh = homem1
else:
    menorh = homem1

total2 = menorh + maiorm

print(f"a idade somada da menor idade homem e maior idade mulher: {total2}")