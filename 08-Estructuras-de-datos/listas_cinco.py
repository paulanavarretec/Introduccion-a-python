import listas_dos as l2


columna = 'mpg'
mayores = list(filter(lambda x : x > l2.mean_values[columna], l2.df[columna]))
print('La lista de valores de mpg mayores a la media es: {}'.format(mayores))    

