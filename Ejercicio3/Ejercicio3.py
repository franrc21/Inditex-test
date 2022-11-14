#!/usr/bin/env python
import requests
import json
import os
from pets import Pets

def main():
    f = open ('output.txt','w')

    #Punto 1 del ejercicio
    username = "franrc"
    json_user = [{"id": 0, "username": "franrc", "firstName": "Francisco", "lastName": "Romero", "email": "correo@correo.com", "password": "1234", "phone": "666666666", "userStatus": 0}]
    response = create_user(json_user)
    f.write("Creamos el usuario " + username + " con los siguientes datos:\n")
    f.write(str(json_user) + "\n\n")
    user_info = get_user_info(username)
    f.write("La información obtenida sobre el usuario " + username + " es:\n")
    f.write(str(user_info) + "\n\n")

    #Punto 2 del ejercicio
    status = 'sold'
    sold_pets = get_pet_list_by_status(status)
    sold_pets_names = get_pets_names(sold_pets)
    f.write('\nLista de mascotas vendidas:\n')
    f.write(str(sold_pets_names) + "\n\n")

    #Punto 3 del ejericio
    pets = Pets(sold_pets_names)
    repeated_names = pets.count_repeated_names()
    f.write("La lista de nombres de mascotas y el número de veces que se repiten los nombres es:\n")
    f.write(str(repeated_names) + "\n\n")

    f.close()



def create_user(json_user: json):
    """Creates a new user in the API.

    Args:
        json_user (json): A json with the information about the user we want to create

    Returns
        The API response to the request
    """
    url = "https://petstore.swagger.io/v2/user/createWithArray"
    response = requests.post(url, json = json_user)
    return response


def get_user_info(username):
    """Gets the information about a user of the API.

    Args:
        username (string): The username of the user that we want to know its info

    Returns:
        A json with the user info
    """
    res = requests.get('http://petstore.swagger.io/v2/user/' + username)
    data = res.json()
    return data

def get_pet_list_by_status(status):
    """Gets the list of pets according to the status parameter.

    Args:
        status (string): The condition that pets must meet in order to appear on the list

    Returns:
        A json with the list of pets
    """
    request_url = 'http://petstore.swagger.io/v2/pet/findByStatus?status=' + status
    res = requests.get(request_url)
    data = res.json()
    return data


def get_pets_names(pets: json):
    """Gets a pet names list with the ID of each one.

    Args:
        pets (json): The json with the list of pets

    Returns:
        A dictionary with the ID and name of each pet
    """
    sold_pets = {}
    for p in pets:
        if 'id' in p and 'name' in p:
            id = p['id']
            name = p['name']
            sold_pets[id] = name
    return sold_pets



if __name__ == '__main__':
    main()