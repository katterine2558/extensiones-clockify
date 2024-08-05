from f_getWorkspaces import getWorkspaces
from f_getProjects import getProjects
from f_getTask import getProjectTask
import configparser
import requests
import json

#Obtiene el ID del espacio de trabajo
workspace = getWorkspaces("WORKSPACE")
ID_workspace =  workspace["id"]
#Obtiene la lista de proyectos que el nombre empiece por 2024
projects =  getProjects(workspace)
ID_Project = next((item['id'] for item in projects if item['name'] == "2024-01 Estaciones ML1_WSP"), None)
#Obtiene las tareas del proyecto
tasks = getProjectTask(ID_workspace,ID_Project)

config = configparser.ConfigParser()
config.read("config.ini")
X_Api_Key = config.get('clockify', 'API_KEY')
headers = {'content-type': 'application/json', 'X-Api-Key': X_Api_Key}

for i in range(len(tasks["Tareas"])) :

    print(f"linea {i+1}")

    #URL
    url = f"https://api.clockify.me/api/v1/workspaces/{ID_workspace}/projects/{ID_Project}/tasks/{tasks["ID"][i]}"
    
    #PUT
    data = {
        "name": tasks["Tareas"][i],
        "status": "DONE"
    }
    #Delete to server
    response = requests.put( url, headers=headers,data=json.dumps(data))
    response = requests.delete(url, headers=headers)


