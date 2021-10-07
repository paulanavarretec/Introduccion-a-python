import sys

try:
    mayor = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    if b > mayor:
        mayor = b

    if c > mayor:
        mayor = c

    print('El número mayor es {}'.format(mayor))

except:

    print('Argumentos inválidos')