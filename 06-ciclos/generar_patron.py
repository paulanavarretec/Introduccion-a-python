n = int(input("Ingrese un número para generar su patrón\n"))

for i in range (1,n+1):
    salida = ''

    for j in range (1,i+1):
        salida = salida + str(j)

    print(salida)
