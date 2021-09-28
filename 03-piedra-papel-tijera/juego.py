import sys
import random


try:
  mov= str(sys.argv[1])
  moves = ['piedra', 'papel', 'tijera']

  if mov in moves:

    comp = ['piedra','papel','tijera'][random.randint(0,2)]
    print('Computador juega',comp)

    if mov == 'piedra' and comp == 'papel':
      print('Perdiste')
    elif mov == 'piedra' and comp == 'tijera':
      print('Ganaste')

    elif mov == 'papel' and comp == 'tijera':
      print('Perdiste')
    elif mov == 'papel' and comp == 'piedra':
      print('Ganaste')

    elif mov == 'tijera' and comp == 'piedra':
      print('Perdiste')
    elif mov == 'tijera' and comp == 'papel':
      print('Ganaste')

    else:
      print('Empataste')
    
  else:
    print('Argumento inválido: Debe ser piedra, papel o tijera')




except:
  print("Parámetros incorrectos")
