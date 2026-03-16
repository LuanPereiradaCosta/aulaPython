lata = int(input('Quantas latas de coca 350ml você quer comprar: '))
garrafa = int(input('Quantas garrafas de coca 600ml você quer comprar:  '))
pet = int(input('Quantas garrafas pet de 2 Litros você quer comprar: '))
litro_lata = (lata*350)/1000
litro_garrafa = (garrafa*600)/1000
litro_pet = (pet*2000)/1000
litros = litro_lata+litro_garrafa+litro_pet
print(f'Você comprou {litros} de refrigerante')
print(f'Você comprou {litro_lata} litros de refri lata')
print(f'Você comprou {litro_garrafa} litros de refri garrafa 600ml')
print(f'Você comprou {litro_pet} litros de refri garrada 2 litros')