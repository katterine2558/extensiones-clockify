from f_getWorkspaces import getWorkspaces
from f_getProjects import getProjects
from f_getRecords import get_records
import configparser
import requests
import json

#Obtiene el ID del espacio de trabajo
workspace = getWorkspaces("NOMBRE_WORKSPACE")
ID_workspace =  workspace["id"]
#Obtiene la lista de proyectos que el nombre empiece por el prefijo
projects =  getProjects(workspace,"2022-")
ID_Project = next((item['id'] for item in projects if item['name'] == "2022-47.04 EyD Ptes nuevos Sant. Quilichao_NUEVO CAUCA"), None)

#Obtiene los registros
records = get_records("2024-01-01","2024-05-28",ID_workspace,ID_Project)

config = configparser.ConfigParser()
config.read("config.ini")
X_Api_Key = config.get('clockify', 'API_KEY')
headers = {'content-type': 'application/json', 'X-Api-Key': X_Api_Key}

cont = 2
for record in records:

    print(f"linea {cont}")
    
    url = f"https://api.clockify.me/api/v1/workspaces/{ID_workspace}/time-entries/{record['_id']}"

   
    #Delete to server
    response = requests.delete( url, headers=headers)

    cont+=1


