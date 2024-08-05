import gspread
import pandas as pd
from f_getUserAPIKEY import f_readUserAPIKEY
from f_getWorkspaces import getWorkspaces
from f_getProjects import getProjects
from f_getTask import getProjectTask
from f_setHour import convert24HFormat, convertUTCHour
import requests
import json

#Lee el archivo de las api de usuarios
file_key = 'ID_FILE'
sheet_name = 'Respuestas de formulario 1'
token_path = 'service_account.json'
user_api = f_readUserAPIKEY(token_path,file_key,sheet_name)
#Obtiene el ID del espacio de trabajo 
workspace = getWorkspaces("ESPACIO DE TRABAJO")
ID_workspace =  workspace["id"]
#Obtiene la lista de proyectos que el nombre empiece por el prefijo
projects =  getProjects(workspace,"2022-")
ID_Project = next((item['id'] for item in projects if item['name'] == "2022-47 EyD Ptes nuevos Sant. Quilichao_NUEVO CAUCA"
), None)
#Obtiene las tareas del proyecto
tasks = getProjectTask(ID_workspace,ID_Project)
# Lee el dataframe
dataframe = pd.read_excel("2022-47.04 Ptes Quilichao.xlsx", sheet_name="Detailed Report")

#URL de conexión
url = f'https://api.clockify.me/api/v1/workspaces/{ID_workspace}/time-entries'

#itera por los usuarios
for i in range(len(dataframe)):

    #Verifica si el usuario tiene clave API
    if dataframe.iloc[i,6] in user_api["Correo"]:

        #Clave api del usuario
        x_api_key = user_api["APIKEY"][user_api["Correo"].index(dataframe.iloc[i,6])]

    else:
        print(f"Linea del Excel {i+1} NO subida. El usuario {dataframe.iloc[i,6]} no tiene API")
        continue
    
    #Verifica tareas
    if dataframe.iloc[i,3] in tasks["Tareas"]:
        taskId = tasks["ID"][tasks["Tareas"].index(dataframe.iloc[i,3])]
    else:
        print(f"Linea del Excel {i+1} NO subida. La tarea no existe")
        continue
    
    #Descripcion
    if pd.isna(dataframe.iloc[i, 2]):
        descripcion = " "
    else:
        descripcion = dataframe.iloc[i,2]

    # Convertir hora en formato 24 horas
    sdate = dataframe.iloc[i,9].strftime('%d/%m/%Y').split('/')
    edate = dataframe.iloc[i,11].strftime('%d/%m/%Y').split('/')
    hIni = dataframe.iloc[i,10].split(' ')
    horaIni = f"{hIni[0]}:00 {hIni[1]}"
    hEnd = dataframe.iloc[i,12].split(' ')
    horaEnd = f"{hEnd[0]}:00 {hEnd[1]}"

    horaI = convert24HFormat(horaIni)
    horaE = convert24HFormat(horaEnd)

    #Convierte la hora colombiana a la del servidor
    start_date = f'{sdate[2]}-{sdate[1]}-{sdate[0]}T{horaI}'
    end_date = f'{edate[2]}-{edate[1]}-{edate[0]}T{horaE}' #Fecha fin de tarea
    start_date = convertUTCHour(start_date)
    end_date = convertUTCHour(end_date)

    data = {
        "start": f"{start_date}Z",
        "description": descripcion,
        "projectId": ID_Project,
        "taskId": taskId,
        "end": f"{end_date}Z"
    }

    headers = {'content-type': 'application/json', 'X-Api-Key': x_api_key}

    response = requests.post( url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print(f"Linea del Excel {i+1} SUBIDA CON EXITO")
    else:
        print(f"Linea del Excel {i+1} NO subida. El usuario {dataframe.iloc[i,6]} no pertenece al workspace")

    a = 10
