import sys

try:
  precio_venta = float(sys.argv[1])
  usuarios = int(sys.argv[2])
  gastos = int(sys.argv[3])

  print("La utilidad es:", (precio_venta * usuarios)-gastos )
except:
  print("Parámetros incorrectos")
