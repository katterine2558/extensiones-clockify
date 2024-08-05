#Importa librerías
import configparser
import requests
import re
import pickle
import os

def getProjectTask(workspace_ID, project_ID):
    

    # URL para obtener los proyectos del workspace
    url_base = f'https://api.clockify.me/api/v1/workspaces/{workspace_ID}/projects/{project_ID}/tasks'

    # Lectura de la clave de la API
    config = configparser.ConfigParser()
    config.read("config.ini")
    X_Api_Key = config.get('clockify', 'API_KEY')

    # Get al servidor
    headers = { 'X-Api-Key': X_Api_Key}
    data = {
            "page-size": 200,
            "page": 1,
        }
    response = requests.get(url_base, headers=headers, params=data)
    decoded_content = response.content.decode('utf-8')
    decoded_content = decoded_content.replace("null","None")
    decoded_content = decoded_content.replace("true","True")
    decoded_content = decoded_content.replace("false","False")
    decoded_content = eval(decoded_content)

    tareas = [decode["name" ]for decode in decoded_content]
    id_tareas = [decode["id" ]for decode in decoded_content]

    return {"Tareas":tareas, "ID":id_tareas}