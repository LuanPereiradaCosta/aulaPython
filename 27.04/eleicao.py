print("Escolha seu voto: ")
print("[1] Lula\n[2] Bolsonaro\n[3] Zega\n[4] Guilherme thesmann\n[5] Nulo\n[6] Branco")
contn = contb = cont1 = cont2 = cont3 = cont4 = cont5 = 0
for e in range(0,5):
    voto = int(input(":"))
    if voto == 1:
        cont1 +=1
    elif voto == 2:
        cont2 += 1
    elif voto == 3:
        cont3 += 1
    elif voto == 4:
        cont4 += 1
    elif voto == 5:
        contb += 1  
    elif voto == 6:
        contn += 1 

print("\n--- Resultado da Eleição ---")
print(f"Lula: {cont1}")
print(f"Bolsonaro: {cont2}")
print(f"Zega: {cont3}")
print(f"Guilherme thesmann: {cont4}")
print(f"Nulo: {contb}")
print(f"Branco: {contn}")

