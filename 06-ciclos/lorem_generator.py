import lorem

n = int(input("Ingrese un número de párrafos a generar\n"))

for i in range(n):
    print(lorem.paragraph())
