#!/usr/bin/env python
# coding: utf-8

# # Prueba - API
# ## Nombre: Paula Navarrete Campos

# # 1.
# 
# Haga una consulta a la API, incluyendo dentro de la request la API Key entregada al 
# momento de registrarse, que recupere la información asociada a las imágenes 
# tomadas por el mars rover. Quédese solo con los 25 primeros registros entregados 
# por la API y descarte los demás.

# In[19]:


import requests
import json


def response(url):
    #url = "https://reqres.in/api/users"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response)
    return(response.text)


url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=NYxTx2dgU9PK5Rk3ueDQb2DjMaeUxS5E4fjfSarW"

rpta = response(url)
results = json.loads(rpta)['latest_photos'][:25]


# In[14]:


results[0].keys()


# # 2.
# Genere una lista que contenga solo las URLs de las imágenes encontradas en el 
# diccionario de respuesta filtrado de la consulta del punto anterior. La lista de URLs 
# debe ser generada mediante código, se considerará como respuesta incorrecta el 
# copy/paste manual de las direcciones en una lista.
# 

# In[21]:


url_list = [photo_dict['img_src'] for photo_dict in results]
(url_list)


# # 3.
# Genere una función llamada build_web_page que debe recibir como parámetro una 
# lista con URLs de imágenes en la web y construir una página web que muestre las 
# fotos.

# In[49]:



def build_web_page(urls):
    
    html = '<!DOCTYPE html>\n'
    html += '<html>\n'
    html += '<head>\n'
    html += '  <title>Mars Rover Photos</title>\n'
    html += '</head>\n'
    html += '<body>\n'
    html += '<ul>\n'
    
    for url in urls:
        html += '  <li><img src=' + url +'></li>\n'
    
    html += '</ul>\n'
    html += '</body>\n'
    html += '</html>\n'
   
    
    return html
    
html = build_web_page(url_list)
print(html)

with open("MarsRover.htm", "w") as text_file:
    text_file.write(html)

