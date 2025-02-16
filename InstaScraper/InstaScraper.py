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

# Obtener el perfil (reemplaza 'nombre_de_usuario' por el perfil deseado)
profile = instaloader.Profile.from_username(L.context, "nombre_de_usuario")

# Descargar las publicaciones solicitadas (incluye fotos, videos y reels)
for i, post in enumerate(profile.get_posts()):
    if i >= num_posts:
        break
    # La carpeta destino será la ruta elegida + nombre de usuario
    target_folder = os.path.join(save_path, profile.username)
    L.download_post(post, target=target_folder)
    time.sleep(1)  # Espera 1 segundo entre descargas