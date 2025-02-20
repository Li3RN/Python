# InstaScraper - Descarga de Publicaciones de Instagram con Ruta Personalizada

Este script permite descargar publicaciones (fotos, videos y reels) de un perfil de Instagram utilizando la librería [Instaloader](https://github.com/instaloader/instaloader). Permite autenticarse (incluyendo la autenticación de dos factores) y elegir tanto el número de publicaciones a descargar como la ruta de guardado (ruta absoluta o relativa).

## Aviso Importante
  Instagram detecta y puede bloquear actividades automatizadas. El uso excesivo o abusivo de este script puede resultar en el cierre temporal o permanente de la cuenta de Instagram. Utiliza este script de manera responsable y de acuerdo con los términos de uso de Instagram. Se recomienda hacer uso moderado y siempre contar con el consentimiento adecuado para evitar consecuencias negativas.
- **Uso Responsable:**
  Asegúrate de cumplir con los términos de uso de Instagram y de respetar la privacidad de los usuarios. Este script se proporciona con fines educativos y para uso personal.

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