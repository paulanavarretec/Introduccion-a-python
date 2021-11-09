import sys
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

def filter_dict(limite , sales = ventas):
    return {k: v for k,v in sales.items() if v > limite }

try:
    limite = int(sys.argv[1])
except:
    limite = 45000

print(filter_dict(limite, ventas))
print(filter_dict(limite))