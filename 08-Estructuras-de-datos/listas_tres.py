import listas_dos as l2

#print(l2.df)
print('Autos con mpg mayor a la media mean_mpg = {}'.format(l2.mean_values['mpg']))
for index, auto in l2.df.iterrows():
    if(auto['mpg'] > l2.mean_values['mpg']):
        print('Modelo: {} \t| mpg: {}'.format(auto['Model'],auto['mpg']))