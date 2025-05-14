a, b, c = map(float,input().split())
pi = 3.14159

#Áreas
atri = (a * c)/2
acir = pi * c **2
atrap = ((a + b)*c)/2
aqua = b * b
aret = a * b

print(f'TRIANGULO: {atri:.3f}')
print(f'CIRCULO: {acir:.3f}')
print(f'TRAPEZIO: {atrap:.3f}')
print(f'QUADRADO: {aqua:.3f}')
print(f'RETANGULO: {aret:.3f}')