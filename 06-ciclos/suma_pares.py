n = int(input("Ingrese un número para comenzar la cuenta de pares\n"))
pares = 0
acumulador = 0
salida = '' + str(pares)

while pares <= n:
    #print('pares {} acumulador {}'.format(pares, acumulador))
    salida = salida + ' + ' + str(pares)
    pares = pares + 2
    acumulador = acumulador + pares

acumulador = acumulador - pares # resto suma excedente del borde
print(salida.replace('0 + ','')) # resto el texto excedente del comienzo
print('La suma de pares hasta el {} corresponde a {}'.format(n,acumulador))