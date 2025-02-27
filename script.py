import os
from dotenv import load_dotenv
import json

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la ruta del archivo JSON
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Abre y lee el JSON con las credenciales (si necesitas parsearlo manualmente)
with open(credentials_path, 'r') as f:
    google_credentials = json.load(f)

print("Credenciales de Google:", google_credentials)