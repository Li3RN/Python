##############################################################################################################
#                                  |                                                                         #
# Title        : InstaScraper      |                           _   ______       _ __                         #
# Language     : Python            |                          / | / / __ \___  (_) /                         #
# Author       : NReiL             |                         /  |/ / /_/ / _ \/ / /                          #
# Version      : 1.0               |                        / /|  / _, _/  __/ / /___                        #
# Category     : Scraper           |                       /_/ |_/_/ |_|\___/_/_____/                        #
# Target       : Instagram         |                                                                         #
# Mode         : ---               |                                                                         #
#__________________________________|_________________________________________________________________________#
#  github.com/Li3RN                                                                                          #
##############################################################################################################

"""
.SYNOPSIS
        Este script pide un número de publicaciones y una carpeta de guardado, se conecta y se autentica en
        instagram y descarga ese número de publicaciones.

.DESCRIPTION
        El script utiliza la librería Instaloader para conectarse a Instagram, autenticar a un usuario
        (manejando la autenticación de dos factores si es necesario), y luego descargar un número específico
        de las publicaciones más recientes (fotos, vídeos y reels) de un perfil de Instagram objetivo.
        El usuario puede especificar el perfil del cual descargar, cuántas publicaciones desea obtener y
        la ruta en el sistema de archivos donde se guardará el contenido descargado.
        El material se organiza en una carpeta con el nombre del perfil dentro de la ruta de guardado.

.LINK
        https://instaloader.github.io/                               # Documentación de Instaloader
        https://github.com/instaloader/instaloader                   # Repositorio de Instaloader en GitHub

"""

import time
import os
import instaloader

# Crear una instancia de Instaloader
L = instaloader.Instaloader(download_video_thumbnails=False)

# Iniciar sesión con manejo de autenticación de dos factores
try:
    L.login("USUARIO_PROPIO", "CONTRASEÑA")
except instaloader.exceptions.TwoFactorAuthRequiredException:
    two_factor_code = input("Introduce el código de autenticación de dos factores: ")
    L.two_factor_login(two_factor_code)

# Solicitar al usuario el número de publicaciones a descargar
num_posts = int(input("¿Cuántas publicaciones deseas descargar? "))

# Solicitar al usuario la ruta de guardado del material
save_path = input("Introduce la ruta de guardado para el material descargado (Puede ser relativa o absoluta): ")

# Verificar si la ruta existe, y si no, crearla
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Obtener el perfil (reemplaza 'NOMBRE_DE_USUARIO' por el perfil deseado)
profile = instaloader.Profile.from_username(L.context, "NOMBRE_DE_USUARIO")

# Descargar las publicaciones solicitadas (incluye fotos, videos y reels)
for i, post in enumerate(profile.get_posts()):
    if i >= num_posts:
        break
    # La carpeta destino será la ruta elegida + nombre de usuario
    target_folder = os.path.join(save_path, profile.username)
    L.download_post(post, target=target_folder)
    time.sleep(1)  # Espera 1 segundo entre descargas
