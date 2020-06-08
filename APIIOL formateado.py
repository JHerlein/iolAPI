import requests
import json

#Ingreso la informacion para pedir la key 

#URL de la API
API_ENDPOINT = "https://api.invertironline.com/token"

#Datos de la cuenta
username = ""
password = ""

#https://api.invertironline.com/token
#POST /token HTTP/1.1
#Host: api.invertironline.com
#Content-Type: application/x-www-form-urlencoded
#username=MIUSUARIO&password=MICONTRASEÑA&grant_type=password

# Informacion para enviar en el request
data = {"username":username,
        "password":password,
        "grant_type": "password"}

#Envio el request y guardo el response

r = requests.post(url = API_ENDPOINT, data = data)

#Parseo el response para usar la info
y = r.json()

#Extraigo el access_token

access_token = y["access_token"]

#Aca esta para pedir el refresh token, siempre use datos rapido, asi que no tengo armado como tengo que usar el refresh token
#Pero aca se los dejo, solamente tiene que agregar una funcion que calcule el tiempo desde el primer llamado, y si supera los
#15 minutos volves a pedir denuevo un token pasando como parametro el refresh token

refresh_token = y["refresh_token"]

data_refresh = {"refresh_token":refresh_token,
                "grant_type":"refresh_token"}

# POST /token HTTP/1.1
# Host: api.invertironline.com
# Content-Type: application/x-www-form-urlencoded
# refresh_token=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb&grant_type=refresh_token

r = requests.post(url = API_ENDPOINT, data = data_refresh )

#Guardo la info para usarla en el proximo header

access_token2 = "Bearer "+ access_token

headers = {"Authorization": access_token2 }

#Genero una request para conseguir los datos de los FCI

FCI = requests.get(url = "https://api.invertironline.com/api/v2/Titulos/FCI", headers = headers)

#Parseo la informacion para poder manipularla

FCI_data = FCI.json()

#Luego ya podemos consultar la informacion dentro del JSON, por ejemplo si queremos consultar la variacion del primer elemento 
# o la de todos los FCI

print(FCI_data[0]["variacion"])


# o la de todos los FCI

for data in FCI_data:
    print("La variacion del FCI " + str(data["descripcion"]) + " fue de " +  str(data["variacion"]))

