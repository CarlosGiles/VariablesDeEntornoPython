# 🌱 Manejo de Variables de Entorno en Python con `.env`

🚀 En este repositorio aprenderás cómo manejar variables de entorno en Python utilizando archivos `.env` de manera segura y eficiente. El archivo que debes revisar a profundidad es el `teoria.md`

## 📌 Contenido
- ¿Qué son las Variables de Entorno?
- ¿Por qué usar archivos `.env`?
- Instalación y configuración
- Carga de variables en Python
- Ejemplo práctico de conexión a una base de datos
- Buenas prácticas
- Alternativa con JSON

## 📥 Instalación

Para comenzar, instala la librería `python-dotenv` ejecutando:
```bash
pip install python-dotenv
```

## 🛠️ Uso

1. Crea un archivo `.env` y define tus variables:
   ```ini
   DB_USER=usuario_db
   DB_PASSWORD=claveSuperSecreta
   API_KEY=abcdef123456
   ```

2. Carga las variables en tu script de Python:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   db_user = os.getenv("DB_USER")
   db_password = os.getenv("DB_PASSWORD")
   ```

3. ¡Listo! Ahora puedes usar estas variables en tu aplicación sin exponer credenciales en el código.

## ⚡ Ejemplo Práctico

Conéctate a una base de datos usando las variables de entorno:
```python
import psycopg2

try:
    connection = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host="localhost",
        port="5432"
    )
    print("✅ Conexión exitosa a la base de datos!")
except Exception as e:
    print(f"❌ Error al conectar: {e}")
```

## ✅ Buenas Prácticas

- **No subas el `.env` a repositorios públicos** (agrega `.env` a tu `.gitignore`).
- **Define valores por defecto** en caso de ausencia:
  ```python
  db_host = os.getenv("DB_HOST", "localhost")
  ```
- **Carga las variables al inicio del script** para evitar problemas de acceso.

## 🔗 Recursos

- 📌 [Repositorio de `python-dotenv`](https://github.com/theskumar/python-dotenv)
- 📌 [Documentación oficial de `os` en Python](https://docs.python.org/3/library/os.html)
