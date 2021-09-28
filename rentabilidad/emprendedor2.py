import sys

try:
  normales= float(sys.argv[1])
  premium = int(sys.argv[2])
  prueba = int(sys.argv[3])
  precio_venta = int(sys.argv[4])
  gastos = int(sys.argv[5])

  utilidad = normales * precio_venta + premium * 2 * precio_venta - gastos

  print("La utilidad es:", utilidad)
except:
  print("Parámetros incorrectos")
