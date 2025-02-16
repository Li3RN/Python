# InstaScraper - Descarga de Publicaciones de Instagram con Ruta Personalizada

Este script permite descargar publicaciones (fotos, videos y reels) de un perfil de Instagram utilizando la librería [Instaloader](https://github.com/instaloader/instaloader). Permite autenticarse (incluyendo la autenticación de dos factores) y elegir tanto el número de publicaciones a descargar como la ruta de guardado (ruta absoluta o relativa).

## Características

- **Autenticación Completa:**  
  Se conecta a Instagram utilizando tus credenciales. Si tu cuenta tiene autenticación de dos factores (2FA), se solicita el código correspondiente.

- **Selección Dinámica:**  
  Permite ingresar el número de publicaciones a descargar y especificar la ruta de guardado para el material descargado. La ruta puede ser relativa (en relación al directorio actual) o absoluta.

- **Soporte para Contenido Variado:**  
  Descarga publicaciones que pueden incluir fotos, videos y reels.

- **Retardo entre Descargas:**  
  Introduce un retardo de 1 segundo entre cada descarga para reducir el riesgo de bloqueos por parte de Instagram.

## Requisitos

- **Python 3.6 o superior**
- **Instaloader:**  
  Instálalo con:
  ```bash
  pip install instaloader

### v1.0.0