⏱️ Clockify API Extensions (Python Scripts)

This repository contains Python scripts designed to extend the functionality of Clockify using its API. These scripts automate common tasks related to project management and time tracking, improving efficiency and simplifying repetitive tasks.
📂 Scripts Overview

    01. Eliminar todos los registros de un proyecto
    Deletes all time entries associated with a specified project.

    02. Eliminar y agregar tareas a un proyecto
    Removes existing tasks and adds new tasks to a specified project.

    03. Cargar horas a proyecto desde Excel
    Imports time entries from an Excel file and uploads them to a specified project.

🔧 Prerequisites

    Python 3.x

    Clockify API Key (obtainable from your Clockify account settings)

    Libraries:
    Install dependencies using pip:

    pip install requests pandas openpyxl

⚙️ How to Use

    Set Up API Key:
    Replace the placeholder YOUR_API_KEY in each script with your actual Clockify API key.

    Run Scripts:
    Execute each script from the terminal:

    python script_name.py

    Configure Project/Task IDs:
    Update project and task IDs within the scripts as needed for your specific use case.

📄 Scripts in Detail
1. Eliminar todos los registros de un proyecto

    Functionality:
    Deletes all time entries for a specific project.

    Usage:
    Modify the project ID in the script before running.

2. Eliminar y agregar tareas a un proyecto

    Functionality:
    Removes all tasks from a project and adds new tasks.

    Usage:
    Specify the project ID and task details in the script.

3. Cargar horas a proyecto desde Excel

    Functionality:
    Reads an Excel file containing time entries and uploads them to a project.

    Usage:
    Prepare an Excel file with columns for project ID, description, hours, etc. Adjust the script to match your Excel format.

🔒 API Key Security

    Keep your API key secure: Avoid sharing or exposing it in public repositories.
    Environment Variables: Consider storing the API key in environment variables instead of hardcoding.

📬 Support

For questions or issues, please open an issue in this repository or contact the project maintainer.
📝 License

This project is licensed under the MIT License.
