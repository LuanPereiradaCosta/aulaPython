nome = "luan pereira".replace(" ", "-")
primeiro = nome[:4]
segundo = nome[5:]
contador = nome.count("a")
trasprafrente = nome[::-1]
doisemdois = nome[::2]
titulo  = nome.title()
maiusculo = nome.capitalize()
print(f"Primeiro {primeiro}\nSegundo: {segundo}\nQuantos a: {contador}\nTrás pra frente: {trasprafrente}\nde dois em dois: {doisemdois}\n")
print(f"Maisculo {maiusculo}\nTitulo: {titulo}")