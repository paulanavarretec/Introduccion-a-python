################################################################################################################
# Desafío - Juegos Olímpicos
################################################################################################################

import pandas as pd

'''
Ejercicio 1
Importar la base de datos athlete_events.csv, y reportar la cantidad de registros 
(filas) y de campos (columnas). El resultado debe guardarse en una variable llamada 
ejercicio_1.
Tip: Puede hacer uso de .shape para esto.
'''

df = pd.read_csv("athlete_events.csv")
ejecicio_1 = df.shape

print('1a.Cantidad de registros: {}'.format(df.shape[0]))
print('1b.Cantidad de campos: {}'.format(df.shape[1]))

'''
Ejercicio 2
Reportar cuántas competencias se han realizado a lo largo del tiempo. El resultado 
debe ser un número entero y debe guardarse en una variable llamada ejercicio_2.
'''

ejercicio_2 = sorted(pd.unique(df['Games'])) # cuántos juegos olímpicos olimpicos se han realizado 
print('\n2.Competencias realizadas a lo largo del tiempo:')
print(ejercicio_2)

'''
Ejercicio 3
Reportar el porcentaje (número entre 0 y 1) de atletas que participaron tanto en los 
juegos olímpicos de Verano como en los de Invierno. El resultado debe guardarse en 
una variable llamada ejercicio_3.
'''

athletes = df.groupby('Name')['Season'].nunique().to_frame(name='unique_seasons')
e_3a = len(athletes[athletes['unique_seasons']>1])/len(athletes) 
e_3b = len(athletes[athletes['unique_seasons']<=1])/len(athletes) 

d = {'Invierno Y Verano': [e_3a]}
ejercicio_3 = pd.DataFrame(data=d)

print('\n3.Porcentaje de Participación de Atletas en juegos de verano e invierno')
print(ejercicio_3)

'''
Ejercicio 4
Informar dónde fue la primera celebración de un Juego Olímpico de Verano. El 
resultado debe guardarse en una variable llamada ejercicio_4.
Tip: Investige sobre las funciones min() y unique() de una Serie de pandas.
'''
first_summer_year = df[df['Season'] == 'Summer']['Year'].min()
#print(first_summer_year)

ejercicio_4 = df.loc[ (df['Year'] == first_summer_year) & (df['Season'] == 'Summer'), ['City']]['City'].unique()
print('\n4.La Primera Celebración de un Juego olimpico de verano fue en',ejercicio_4[0])

'''
Ejercicio 5
Informar dónde fue la primera celebración de un Juego Olímpico de Invierno. El 
resultado debe guardarse en una variable llamada ejercicio_5.
'''                            

first_winter_year = df[df['Season'] == 'Winter']['Year'].min()

ejercicio_5 = df.loc[ (df['Year'] == first_winter_year) & (df['Season'] == 'Winter'), ['City']]['City'].unique()
print('\n5.La Primera Celebración de un Juego olimpico de invierno fue en',ejercicio_5[0])



'''
Ejercicio 6
Reportar los 10 primeros países con mayor cantidad de atletas participantes a lo largo 
de los juegos. El resultado debe guardarse en una variable llamada ejercicio_6.

'''

ejercicio_6 = list(df.groupby('NOC')['Name'].nunique().to_frame(name='unique athletes').sort_values(ascending=False, by='unique athletes').head(10).index)

print('\n6. Países con mayor cantidad de atletas participantes a lo largo de los juegos')
print(ejercicio_6)

'''
Ejercicio 7
Reportar el porcentaje de medallas asignadas (oro, bronce, plata). El resultado debe 
guardarse en una variable llamada ejercicio_7.
'''


gold = len(df[df['Medal'] == 'Gold'])/len(df[df.Medal.notnull()]) 
silver = len(df[df['Medal'] == 'Silver'])/len(df[df.Medal.notnull()]) 
bronze = len(df[df['Medal'] == 'Bronze'])/len(df[df.Medal.notnull()]) 

d = {'% Oro': [gold], '% Plata': [silver], '% Bronce':[bronze]}
ejercicio_7 = pd.DataFrame(data=d)

print('\n7. Porcentaje de medallas asignadas')
print(ejercicio_7)

'''
Ejercicio 8
Reportar cuáles fueron los países participantes en las primeras olimpiadas de verano. 
El resultado debe guardarse en una variable llamada ejercicio_8.
'''

first_summer_year = df[df['Season'] == 'Summer']['Year'].min()
ejercicio_8 = df.loc[ (df['Year'] == first_summer_year) & (df['Season'] == 'Summer'), ['NOC']]['NOC'].unique()

print('\n8.Los países participantes en las primeras olimpiadas de verano son:')
print(ejercicio_8)


################################################################################################################
# Desafío Opcional - El caso de Chile
################################################################################################################

'''
1. Generar un nuevo subset a partir del DataFrame original, que almacene todas las
observaciones correspondientes a Chile.
'''

chile = df[df['NOC']=='CHI' ]

print('\nChile1. Observaciones correspondientes a Chile')
print((chile))

'''
2. Utilizando el subset generado, reportar la cantidad de atletas chilenos registrados en
cada año, y en qué año hubo la participación más alta.
'''
print('\nChile2a. Cantidad de atletas chilenos registrados por año')
chile_2 =  chile.groupby('Year')['Name'].nunique().to_frame(name='unique athletes').sort_values(ascending=False, by='unique athletes')
print(chile_2)
print('\nChile32b El año con mayor cantidad de atletas chilenos registrados fue {}'.format(chile_2.head(1).index[0]))

'''
3. Reportar los nombres de todos los ganadores de alguna medalla.
'''

print('\nChile3.Los ganadores de alguna medalla son:')
chile_3 = pd.Series(chile.loc[chile.Medal.notnull(),'Name'].unique(),name='winners')
print(chile_3)

'''
4. Reportar en qué año Chile obtuvo más medallas.

'''

chile_4 = chile.loc[chile.Medal.notnull()]
chile_4 =  chile_4.groupby('Year')['ID'].nunique().to_frame(name='medallas').sort_values(ascending=False, by='medallas').head(1).index[0]

print('\nChile4. El año en que Chile obtuvo más medallas fue:')
print(chile_4)