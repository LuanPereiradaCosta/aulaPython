real1 = int(input("Quantas moedas de 1 real tem: "))
cent50 = int(input("Quantas moedas de 50 centavos tem: "))
cent25 = int(input("Quantas moedas de 25 centavos tem: "))
cent10 = int(input("Quantas moedas de 10 centavos tem: "))
cent5 = int(input("Quantas moedas de 5 centavos tem: "))
cent1 = int(input("Quantas moedas de 1 centavo tem: "))
soma = (real1*1)+(cent50*0.50)+(cent25*0.25)+(cent10*0.10)+(cent5*0.05)+(cent1*0.01)

print(f"Foram economizados R${soma}")