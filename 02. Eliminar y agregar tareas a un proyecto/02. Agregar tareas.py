from f_getWorkspaces import getWorkspaces
from f_getProjects import getProjects
from f_getTask import getProjectTask
import configparser
import requests
import json
import pandas as pd

#Obtiene el ID del espacio de trabajo de ¿
workspace = getWorkspaces("WORKSPACE")
ID_workspace =  workspace["id"]
#Obtiene la lista de proyectos que el nombre empiece por 2024
projects =  getProjects(workspace)
ID_Project = next((item['id'] for item in projects if item['name'] == "2024-01 Estaciones ML1_WSP"), None)
#Lee el archivo de tareas
dataframe = pd.read_excel("Tareas 2024-01.xlsx", sheet_name="Tareas Clockify 2024-01", header=None)

config = configparser.ConfigParser()
config.read("config.ini")
X_Api_Key = config.get('clockify', 'API_KEY')
headers = {'content-type': 'application/json', 'X-Api-Key': X_Api_Key}


for i in range(len(dataframe)):

    print(i)
    url = f"https://api.clockify.me/api/v1/workspaces/{ID_workspace}/projects/{ID_Project}/tasks"

    data = {
        "name": dataframe.iloc[i,0]
    }
   
    #post to server
    response = requests.post( url, headers=headers, data = json.dumps(data))