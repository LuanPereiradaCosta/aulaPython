n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    maior = n1
    menor = n2
elif n1 < n2:
    maior = n2
    menor = n1
else:
    maior = n1 
    menor = n2

total = maior - menor 
print(f"A diferença do maior para o menor {total}")