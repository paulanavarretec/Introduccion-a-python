import sys

try:
  precio_venta = float(sys.argv[1])
  usuarios = int(sys.argv[2])
  gastos = int(sys.argv[3])

  try:
    utilidades_ant = int(sys.argv[4])
  except:
    utilidades_ant = 1000


  utilidad = precio_venta * usuarios- gastos
  razon = float(utilidad/utilidades_ant)

  print("La utilidad actual es:", utilidad)
  print("La razón con año anterior es:", razon)
except:
  print("Parámetros incorrectos")
