

"""
- El usuario ingresa debe ingresar un password en la plataforma. Si el password tiene
menos de 6 letras, se debe mostrar un aviso.
- El usuario debe ingresar un password. Si el password es 12345, se debe informar
que el password es incorrecto
"""

import sys

password = input('Ingrese su password: ')

if len(password) < 6:
    print('Advertencia: Su password tiene menos de 6 caracteres')

if password == '12345':
    print('Advertencia: Su password es incorrecto')
