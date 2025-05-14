c1, n1, vu1 = map(float, input().split())
c2, n2, vu2 = map(float, input().split())

valor = int(n1) * float(vu1) + int(n2) * float(vu2)

print(f'VALOR A PAGAR: R$ {valor:.2f}')
