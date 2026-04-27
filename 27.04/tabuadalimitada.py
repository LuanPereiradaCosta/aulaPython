num = int(input("Digite o número da tabuada:: "))
com = int(input("Digite aonde começa: "))
fim = int(input("Digite aonde termina: "))
for t in range (com, fim+1):
    total = t*num
    print(f"{num} x {t} = {total}")