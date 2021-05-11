print("Olá mundo!")

valor = int(input("valor para sacar [10 - 600]: " ))
cem = valor // 100
valor = valor - (cem*100)

cinquenta = valor // 50
valor -= valor - (cinquenta*50)

dez = valor // 10
valor -= valor - (dez*10)

cinco = valor // 5
valor -= valor - (cinco*5)

um = valor

print(f'Notas de R$ 100.00: {cem} ')
print(f'Notas de R$ 50.00: {cinquenta} ')
print(f'Notas de R$ 10.00: {dez} ')
print(f'Notas de R$ 5.00: {cinco} ')
print(f'Notas de R$ 1.00: {um} ')