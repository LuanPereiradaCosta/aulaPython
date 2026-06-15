tab = int(input("Qual tabuada deseja: "))
init = int(input("Quando inicia: "))
end = int(input("Quando termina: "))
while init <= end:
    print(f"{tab} x {init} = {tab  * init}")
    init +=1