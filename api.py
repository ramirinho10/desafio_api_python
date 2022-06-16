import requests
import json

url = "https://reqres.in/api/users"
headers = {}
payload = {}

def request_get(url):
    return json.loads(requests.get(url).text)

response = request_get(url)


def resp(metodo, url, headers, payload):
    response = requests.request(metodo, url, headers=headers, data=payload).text
    return response


"""
1. Obtenga toda la información de los usuarios retornada por la API, guárdela en una
variable llamada users_data e imprímala en pantalla.
"""

users_data = response['data']
print(users_data)


"""
2. Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el
diccionario de respuesta en una variable llamada created_user e imprímala en
pantalla.
"""

url_2 = "https://reqres.in/api/users"


payload_2 = '''{
            "name": "Ignacio",
            "trabajo": "Profesor"
            }
        '''

headers_2 = {
    'Content-Type': 'application/json'
}

created_user = resp("POST", url_2, headers_2, payload_2)
print(created_user)

"""
3. Actualice un usuario llamado morpheus para que tenga un campo llamado
residence igual a zion. Guarde el diccionario de respuesta en una variable llamada
updated_user e imprímala en pantalla.
"""

url_3 = "https://reqres.in/api/users/1"

payload_3 = '''{
        "id": 1,
        "email": "morpheus.bluth@reqres.in",
        "first_name": "Morpheus",
        "last_name": "Bluth",
        "avatar": "https://reqres.in/img/faces/1-image.jpg",
        "residence": "Zion"
    }
        '''

headers_3 = {
    'Content-Type': 'application/json'
}

update_user = resp("PUT", url_3, headers_3, payload_3)
print(update_user)


"""
4. Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla.
"""

url_4 = "https://reqres.in/api/users/6"

lista = (response['data'])

#Saco el id del usuario Tracey
for i in lista:
    cont = 0
    for k,v in i.items():
        if i[k] == "Tracey":
            print(i)
            break


delete_user = resp("DELETE", url, headers, payload)
print(delete_user)