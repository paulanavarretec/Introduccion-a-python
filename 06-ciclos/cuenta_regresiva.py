'''Reemplaza la instrucción for por while 
cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
for i in range(cuenta_regresiva):
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))
'''

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

while cuenta_regresiva > 0:
    
    print("Iteración {}".format(cuenta_regresiva))
    cuenta_regresiva = cuenta_regresiva-1
    
