import sys

##########################
# Creamos las funciones solicitadas
def mostrar_menu(saldo = 0):

    opcion = ''
    error = False
    while opcion not in [1,2,3,4]:
        if error:
            print('Opción inválida. Por favor ingrese 1, 2, 3 ó 4.\n')

        print("Bienvenido al portal del Banco Amigo. Escoja una opción: \n1. Consultar saldo\n2. Hacer depósito\n3. Realizar giro\n4. Salir")
        
        try:
            opcion = int(input())
        except:
            error = True
        
        if opcion not in [1,2,3,4]:
            error = True
    return opcion

def depositar (saldo, cantidad):
    return saldo + cantidad

def girar(saldo, cantidad):
    if saldo >= cantidad:
        return saldo - cantidad
    else:
        return False


#############################################
# Chequeamos la linea de argumentos
saldo = 0
if len(sys.argv)==1 :
    saldo = 0
else:   
    try:
        saldo = int(sys.argv[1])
    except:
        print('Ingrese un argumento numérico por favor.\nSaldo = 0')

##########################
# Chequeamos la opción deseada
opcion = mostrar_menu()

while opcion != 4:
    if opcion == 1:
        print("Su saldo actual es: {}".format(saldo))

    elif opcion == 2:
        print('Ingrese Monto a dopositar:')
        deposito = int(input())
        saldo = depositar(saldo , deposito)
        print("Monto Depositado.\nSu saldo actual es de {}".format(saldo))

    elif opcion == 3:
        print('Ingrese Monto a girar:')
        giro = int(input())

        if(saldo == 0):
            print('No puede realizar giros. Su saldo es 0')

        else:
            saldo = girar(saldo , giro)
            
            if saldo == False:
                    
                print('"No se puede girar esta cantidad.'.format(saldo))
            else:
                print("Monto Girado.\nSu saldo actual es de {}".format(saldo))

    opcion = mostrar_menu()

print('Adios! gracias por operar con tu Banco Amigo!')

