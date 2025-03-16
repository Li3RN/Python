# WebhookSender - Automatización de Envío de Archivos a Discord

Este script permite recorrer una carpeta para subir cada archivo a un Webhook de Discord en mensajes individuales, eliminando los archivos enviados correctamente. La configuración se realiza de forma segura mediante un archivo `.env`.

## Aviso Importante :warning:
El uso inadecuado o excesivo de envíos automatizados a Discord puede generar bloqueos o restricciones en el Webhook.  
- **Uso Responsable:** :white_check_mark:  
  Asegúrate de cumplir con los [términos de uso de Discord](https://discord.com/terms) y de configurar el script de manera que se adapte a las políticas de tu servidor. Este script se proporciona con fines educativos y para uso personal.

## Características :star:

- **Automatización Total:** :gear:  
  Recorre automáticamente una carpeta especificada para enviar cada archivo de forma individual.

- **Integración con Discord:** :robot:  
  Envía mensajes personalizados a través de un Webhook, incluyendo el nombre del archivo en cada mensaje.

- **Eliminación Automática:** :wastebasket:  
  Elimina cada archivo enviado correctamente para evitar duplicados.

- **Configuración Segura:** :file_folder:  
  Utiliza un archivo `.env` para definir la URL del Webhook y la ruta de la carpeta, manteniendo tus credenciales protegidas.

## Requisitos :clipboard:

- **Python 3.6 o superior**

- **Librerías:**
  - [requests](https://pypi.org/project/requests/)  
    Instálala con:
    ```bash
    pip install requests
    ```
  - [python-dotenv](https://pypi.org/project/python-dotenv/)  
    Instálala con:
    ```bash
    pip install python-dotenv
    ```

## Instalación y Configuración

1. **Clona el repositorio o descarga el script:**
   ```bash
   git clone <URL-del-repositorio>
   cd <directorio-del-repositorio>
   ```

2. **Crea y activa un entorno virtual (opcional, pero recomendado):**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install requests python-dotenv
   ```

4. **Configura el archivo `.env`:** 
   Crea un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:
   ```env
   WEBHOOK_URL=https://discord.com/api/webhooks/tu_webhook_url
   FOLDER_PATH=C:\ruta\hacia\la\carpeta
   ```

   *Nota:* Si utilizas otro nombre para el archivo de variables, modifica la función `load_dotenv()` en el script para que apunte a dicho archivo.

5. **Protege tus credenciales:** 
   Añade el archivo `.env` a tu `.gitignore` para evitar que se suba al repositorio:
   ```bash
   echo ".env" >> .gitignore
   ```

## Uso

Ejecuta el script desde la línea de comandos:

```bash
python webhook_sender.py
```

El script recorrerá la carpeta especificada en `FOLDER_PATH` y enviará cada archivo a través del Webhook configurado en `WEBHOOK_URL`. Si el envío es exitoso (códigos de respuesta 200 o 204), el archivo se eliminará automáticamente del directorio.

## Documentación

Para más detalles sobre la configuración y uso de Webhooks en Discord, consulta la [Documentación de Webhooks de Discord](https://discord.com/developers/docs/resources/webhook).

## Autor

**NReiL** - Visita [github.com/Li3RN](https://github.com/Li3RN) para más proyectos.

## Licencia

Distribuido bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
