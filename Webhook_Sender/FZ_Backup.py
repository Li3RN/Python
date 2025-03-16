##############################################################################################################
#                                  |                                                                         #
# Title        : WebhookSender     |                           _   ______       _ __                         #
# Language     : Python            |                          / | / / __ \___  (_) /                         #
# Author       : NReiL             |                         /  |/ / /_/ / _ \/ / /                          #
# Version      : 1.0               |                        / /|  / _, _/  __/ / /___                        #
# Category     : Backup            |                       /_/ |_/_/ |_|\___/_/_____/                        #
# Target       : ---               |                                                                         #
# Mode         : ---               |                                                                         #
#__________________________________|_________________________________________________________________________#
#  github.com/Li3RN                                                                                          #
##############################################################################################################

"""
.SYNOPSIS
        Este script recorre una carpeta y sube todos los archivos a un webhook de Discord en mensajes independientes.

.DESCRIPTION 
        Se debe especificar la rute de la carpeta y la URL del Webhook en el archivo .env
        Para cada archivo en la carpeta especificada, se envía un mensaje a Discord con el formato:
        "¡Còpia de NOMBRE DEL ARCHIVO.ext!"
        Luego, si el archivo se sube correctamente, se elimina de la carpeta.

.LINK
        https://discord.com/developers/docs/resources/webhook        # Documentación de Webhooks de Discord

"""

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

url = os.environ.get("WEBHOOK_URL")
if url is None:
    raise ValueError("La variable de entorno WEBHOOK_URL no está configurada.")

# Ruta de la carpeta que contiene los archivos
folder_path = os.environ.get("FOLDER_PATH")
if folder_path is None:
    raise ValueError("La variable de entorno FOLDER_PATH no está configurada.")

# Iterar sobre todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    # Verificar que sea un archivo (no una subcarpeta)
    if os.path.isfile(file_path):
        # Definir el contenido del mensaje usando el nombre del archivo
        payload = {
            "content": f"¡Còpia de {filename}!"
        }
        # Abrir el archivo en modo binario y enviarlo
        with open(file_path, "rb") as f:
            files = {
                "payload_json": (None, json.dumps(payload), "application/json"),
                "file": (filename, f)
            }
            response = requests.post(url, files=files)
            
            # Comprobar el resultado de la petición
            if response.status_code in [200, 204]:
                print(f"Mensaje y archivo '{filename}' enviados correctamente.")
            else:
                print(f"Error al enviar el mensaje para '{filename}': {response.status_code}")