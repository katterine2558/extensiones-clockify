import configparser
import requests
# Obtiene los workspaces de Clockify
def getWorkspaces(workspace_name):
    """
    Input args:
    Output args:
    """

    # URL para obtener los workspaces
    url_base = f'https://api.clockify.me/api/v1/workspaces'
    # Lectura de la clave de la API 
    config = configparser.ConfigParser()
    config.read('config.ini') 
    X_Api_Key = config.get('clockify', 'API_KEY')
    # Get al servidor
    headers = { 'X-Api-Key': X_Api_Key}
    response = requests.get(url_base, headers=headers)
    decoded_content = response.content.decode('utf-8')

    try:
        decoded_content = decoded_content.replace("null","None")
    except:
        pass
    try:
        decoded_content = decoded_content.replace("true","True")
    except:
        pass
    try:
        decoded_content = decoded_content.replace("false","False")
    except:
        pass

    decoded_content = eval(decoded_content)

    #Solo devuelve el espacio de trabajo seleccionado
    for value in decoded_content:
        if value["name"] == workspace_name:
            return value
