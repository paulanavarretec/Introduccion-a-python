import velocidad as vel
import listas_uno as l1
import pandas as pd

df = pd.DataFrame(l1.autos,columns = ['Model','mpg','cyl','vs','carb'])

mean_values = {}

for column in ['mpg','cyl','carb'] :

    avg_numeric = vel.promedio(df[column])        
    mean_values.update({column : avg_numeric})


#print(mean_values)

