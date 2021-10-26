velocidad =[4, 4, 7, 7, 8, 9, 10, 10, 10,
            11, 11, 12, 12, 12, 12, 13, 13,
            13, 13, 14, 14, 14, 14, 15, 15,
            15, 16, 16, 17, 17, 17, 18, 18,
            18, 18, 19, 19, 19, 20, 20, 20,
            20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
            17, 28, 14, 20, 24, 28, 26, 34, 34,
            46, 26, 36, 60, 80, 20, 26, 54, 32,
            40, 32, 40, 50, 42, 56, 76, 84, 36,
            46, 68, 32, 48, 52, 56, 64, 66, 54,
            70, 92, 93, 120, 85]

avg_vel = sum(velocidad)/(len(velocidad))
avg_dist = sum(distancia)/(len(distancia))

# Velocidad bajo el promedio.
e1 = 0
# Velocidad bajo el promedio y distancia sobre el promedio.
e2 = 0
# Velocidad sobre el promedio.
e3 = 0
# Velocidad sobre el promedio y distancia bajo el promedio.
e4 = 0


for i in zip(velocidad, distancia):
    vel = i[0]
    dist= i[1]

    if vel < avg_vel: # Velocidad bajo el promedio.
        e1 += 1
    if (vel < avg_vel) and (dist > avg_dist): # Velocidad bajo el promedio y distancia sobre el promedio.
        e2 += 1
    if vel > avg_vel:# Velocidad sobre el promedio.
        e3 += 1
    if (vel > avg_vel) and (dist < avg_dist): #  Velocidad sobre el promedio y distancia bajo el promedio.
        e4 += 1

print('La cantidad de eventos de Velocidad bajo el promedio fue de {}.'.format(e1))
print('La cantidad de eventos de Velocidad bajo el promedio y distancia sobre el promedio fue de {}.'.format(e2))
print('La cantidad de eventos de Velocidad sobre el promedio fue de {}.'.format(e3))
print('La cantidad de eventos de Velocidad sobre el promedio y distancia bajo el promedio fue de {}.'.format(e4))



