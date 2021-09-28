import sys
import math

try:
  g = float(sys.argv[1])
  r = float(sys.argv[2])

  print("La velocidad de escape es:", math.sqrt(2*g*r) )
except:
  print("Parámetros incorrectos")
