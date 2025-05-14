valor = float(input())

 #notas
notas100 = int(valor // 100)
valor = valor % 100

notas50 = int(valor // 50)
valor = valor % 50

notas20 = int(valor // 20)
valor = valor % 20

notas10 = int(valor // 10)
valor = valor % 10

notas5 = int(valor // 5)
valor = valor % 5

notas2 = int(valor // 2) 
valor = valor % 2 

#moedas
moedas1 = int(valor // 1)
valor = valor % 1

moedas05 = int(valor // 0.5)
valor = valor % 0.5

moedas025 = int(valor // 0.25)
valor = valor % 0.25

moedas010 = int(valor // 0.10)
valor = valor % 0.10

moedas005 = int(valor // 0.05)
valor = valor % 0.05

moedas001 = (valor / 0.01)

print('NOTAS:')
print(f'{notas100} nota(s) de R$ 100.00')
print(f'{notas50} nota(s) de R$ 50.00')
print(f'{notas20} nota(s) de R$ 20.00')
print(f'{notas10} nota(s) de R$ 10.00')
print(f'{notas5} nota(s) de R$ 5.00')
print(f'{notas2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moedas1} moeda(s) de R$ 1.00')
print(f'{moedas05} moeda(s) de R$ 0.50')
print(f'{moedas025} moeda(s) de R$ 0.25')
print(f'{moedas010} moeda(s) de R$ 0.10')
print(f'{moedas005} moeda(s) de R$ 0.05')
print(f'{moedas001:.0f} moeda(s) de R$ 0.01')


