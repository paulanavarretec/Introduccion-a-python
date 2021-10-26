import listas_dos as l2


print('Autos con vs  (vs = True)')
for index, auto in l2.df.iterrows():
    if auto['vs'] :
        print('Modelo:{} \t| mpg: {}\t| cyl: {}\t| carb: {}| vs: {}'.format(auto['Model'],auto['mpg'],auto['cyl'],auto['carb'],auto['vs']))