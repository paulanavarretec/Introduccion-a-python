
abc = 'abcdefghijklmnopqrstuvwxyz'

password = input("Ingresa la contraseña\n").lower()
valida = True
intentos = 0

for i in range(len(password)):
    if password[i] not in abc:
        print('Contraseña Inválida, por favor ingrese solo caracteres alfabéticos')
        valida = False

if valida:
    for i in range(len(password)):
        for j in range(len(abc)):

            intentos = intentos + 1
            if password[i] == abc[j]:
                break
            
                

    print('{} intentos para decifrar {}'.format(intentos, password))