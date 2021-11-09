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

quarters = {}

for k , v in ventas.items():
    
    if k in ['Enero','Febrero','Marzo']:
        key = 'Q1'
    elif k in ['Abril','Mayo','Junio']:
        key = 'Q2'
    elif k in ['Julio','Agosto','Septiembre']:
        key = 'Q3'
    else:
        key = 'Q4'

    try:
        values = quarters[key]
        values.append(v)
        quarters[key] = values
    except:
        quarters[key] = list([v])


print(quarters)