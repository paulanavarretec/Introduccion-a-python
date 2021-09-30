import sys

try:
    mayor = sorted([int(sys.argv[1]), int(sys.argv[2]) , int(sys.argv[3])],reverse=True)[0]
    print("El número mayor es el {}".format(mayor))
except:
    print("Debes ingresar tres numeros")

