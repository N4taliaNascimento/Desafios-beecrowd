a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior_ab = (a + b + abs(a - b)) /2
maiorab_c = (maior_ab + c +abs(maior_ab - c)) / 2

print(f'{int(maiorab_c)} eh o maior')