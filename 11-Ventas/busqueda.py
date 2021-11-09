import sys
from itertools import groupby

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

def busqueda(valor, sales = ventas):
    inverted = {v: k for k,v in sales.items()}
    
    try:
        return inverted[valor]
    except:
        return 'no encontrado'


if len(sys.argv) > 1:
    for valor in sys.argv[1:]:
        print(busqueda(int(valor)))

