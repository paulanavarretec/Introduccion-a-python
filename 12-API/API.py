#!/usr/bin/env python
# coding: utf-8

# # Desafío 1
# 
#  Obtenga toda la información de los usuarios retornada por la API, guárdela en una
# variable llamada users_data e imprímala en pantalla.
# 

# In[1]:


import requests
import json

def response(url):
    #url = "https://reqres.in/api/users"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response)
    return(response.text)
rpta = response("https://reqres.in/api/users")

results = json.loads(rpta)
users_data = results['data']
for user in users_data:
    print(user)


# # Desafío 2
# 
# Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el
# diccionario de respuesta en una variable llamada created_user e imprímala en
# pantalla.
# 

# In[2]:


import requests
import json

url = "https://reqres.in/api/users"

def post(url):
    payload = json.dumps({
      "nombre"  : "Ignacio",
      "trabajo" : "Profesor"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response)
    return(response.text)

created_user = json.loads(post(url))
print(created_user)


# # Desafío 3
# 
# Actualice un usuario llamado morpheus para que tenga un campo llamado
# residence igual a zion. Guarde el diccionario de respuesta en una variable llamada
# updated_user e imprímala en pantalla.

# In[3]:


import requests
import json

url = "https://reqres.in/api/users"
def update(url):
    

    payload = json.dumps({
      "nombre": "Morpheus",
      "residence": "Zion"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response)
    return(response.text)

updated_user = update(url)
print(updated_user)


# # Desafío 4
# 
# Elimine un usuario llamado Pepe. Imprima el código de respuesta en pantalla.
# 

# In[4]:


import requests
import json

url = "https://reqres.in/api/users"
def delete(url):
    

    payload = json.dumps({
      "nombre": "Pepe"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response)
    return(response.text)

deleted_user = delete(url)

