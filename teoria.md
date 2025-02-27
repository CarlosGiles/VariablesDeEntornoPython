# Manejo de Variables de Entorno con Archivos `.env` en Python

En este documento aprenderás a manejar variables de entorno en Python haciendo uso de archivos `.env`. Al finalizar, tendrás una mejor comprensión de qué son las variables de entorno, por qué son útiles, y cómo integrarlas en tus proyectos.

---

## 1. ¿Qué son las Variables de Entorno?

Las **variables de entorno** son valores que pueden afectar el comportamiento de procesos en tiempo de ejecución. En el contexto de aplicaciones, suelen utilizarse para definir configuraciones sensibles o específicas del entorno donde corre la aplicación, por ejemplo:
- **Credenciales**: Usuarios, contraseñas, tokens de acceso
- **URLs** o rutas de servicios externos
- **Flags** de configuración o parámetros que pueden variar según el ambiente (desarrollo, pruebas, producción)

### ¿Por qué usarlas?
- **Separación de configuración del código**: Mantener variables sensibles o de configuración (como credenciales) fuera del código fuente, para no exponer información privada.
- **Flexibilidad**: Permite cambiar comportamientos según el entorno en el que se ejecute (por ejemplo, apuntar a una base de datos de prueba o producción sin cambiar el código).
- **Seguridad**: Evitamos almacenar claves o contraseñas en texto plano dentro del repositorio (por ejemplo, en GitHub).

---

## 2. ¿Por qué `.env`?

Un archivo `.env` se utiliza para mantener las variables de entorno en un formato fácilmente legible y modificable. Por convención, se suele llamar `.env` (sin nombre previo) y se excluye del control de versiones (`.gitignore`) para no exponer información sensible en repositorios públicos.

Un archivo `.env` típicamente luce así:

```
DB_USER=usuario_db
DB_PASSWORD=claveSecreta
API_KEY=abcdef123456
```

---

## 3. Configuración Inicial

Antes de empezar, necesitamos instalar la librería `python-dotenv`, que nos ayuda a **cargar** los valores del archivo `.env` en las variables de entorno del sistema (disponibles a través de `os.environ`).

Ejecuta en tu terminal o en una celda de Jupyter Notebook:

```bash
!pip install python-dotenv
```

---

## 4. Creando un archivo `.env`

En tu proyecto, crea un archivo llamado `.env` (asegúrate de no subirlo a repositorios públicos). Por ejemplo:

```
# Ejemplo de configuración en .env
DB_NAME=mi_base_de_datos
DB_USER=mi_usuario
DB_PASS=mi_contraseña
SECRET_KEY=superSecreto
```

---

## 5. Cargando las Variables de Entorno en Python

La librería `python-dotenv` provee la función `load_dotenv()`, que leerá el archivo `.env` y cargará sus valores dentro de `os.environ`. 

En tu código Python (o en una celda de tu Jupyter Notebook), harás algo como esto:

```python
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Ahora las variables de entorno están disponibles en os.environ
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
secret_key = os.getenv("SECRET_KEY")

print("Base de datos:", db_name)
print("Usuario:", db_user)
print("Contraseña:", db_pass)
print("Llave secreta:", secret_key)
```

**Nota**: `os.getenv("NOMBRE_VARIABLE")` devuelve `None` si la variable no está definida, por lo que es útil para comprobar la existencia de la variable antes de usarla. 

---

## 6. Ejemplo Práctico

Imagina que tenemos un pequeño script que se conecta a una base de datos (ficticia para este ejemplo). Usaríamos las variables de entorno en lugar de hardcodear los valores:

```python
import os
from dotenv import load_dotenv
# Librería hipotética para conectarse a Postgres (a modo de ejemplo)
import psycopg2

# Cargar variables .env
load_dotenv()

def conectar_db():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host="localhost",  # Suponiendo conexión local
            port="5432"
        )
        print("Conexión exitosa a la base de datos!")
        return connection
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None

# Ejecutamos la función
db_connection = conectar_db()

if db_connection:
    # Aquí iría la lógica de tu programa (consultas, inserciones, etc.)
    db_connection.close()
```

De esta manera, si cambias tu base de datos o las credenciales, **solo** modificarías tu archivo `.env`, sin tocar el código.

---

## 7. Buenas Prácticas

1. **Incluir el `.env` en `.gitignore`**: Nunca subas tu archivo `.env` a repositorios públicos.  
2. **Manejar los valores por defecto**: Algunas variables pueden requerir un valor por defecto para que tu aplicación no falle si no encuentra la variable de entorno. Ejemplo:
   ```python
   db_host = os.getenv("DB_HOST", "localhost")
   ```
3. **Usar entornos virtuales**: Mantén un entorno virtual (con `venv`, `conda`, etc.) para instalar `python-dotenv` y otras dependencias sin ensuciar tu instalación global de Python.
4. **Buena organización**: Coloca tu llamada a `load_dotenv()` en la parte superior del script o dentro de tu configuración inicial para que las variables estén disponibles en todo tu proyecto.
5. **Validar**: A veces, es útil validar que las variables requeridas existen (por ejemplo, usando un pequeño script que verifique que todas las variables esenciales estén definidas).

---

## 8. Mediante un archivo JSON

Aunque lo más común para manejar variables de entorno sea emplear archivos `.env` (con librerías como `python-dotenv`), también puedes lograr algo similar usando archivos JSON. Aquí aprenderás cómo.

### 1. ¿Por qué usar JSON para configurar variables?

* Estructura: JSON es un formato muy conocido, legible y fácil de parsear en Python.
* Flexibilidad: Puedes agrupar variables relacionadas, listas, o incluso objetos más complejos, y cargarlos de forma ordenada.
* Usabilidad: Puede que, por políticas o por gustos del equipo, quieran usar un solo archivo JSON que incluya toda la configuración de la aplicación.

>Importante: Aun así, es recomendable no exponer credenciales sensibles en repositorios públicos. Asegúrate de incluir tu archivo JSON en el archivo .gitignore cuando sea sensible.

### 2. ¿Cómo usarlo en tu código?

1. Instala (si aún no lo hiciste) la librería python-dotenv:

```bash
pip install python-dotenv
```

2. Crea un archivo .env (y agré­galo a tu `.gitignore` si contiene datos sensibles) con la línea, por ejemplo:

`GOOGLE_API_CREDENTIALS=api_google.json`

En tu script Python, usa `load_dotenv` para leer el archivo .env y obtén la ruta con `os.getenv`:

```python
import os
from dotenv import load_dotenv
import json

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la ruta del archivo JSON
credentials_path = os.getenv("GOOGLE_API_CREDENTIALS")

# Abre y lee el JSON con las credenciales (si necesitas parsearlo manualmente)
with open(credentials_path, 'r') as f:
    google_credentials = json.load(f)

print("Credenciales de Google:", google_credentials)
```

---

## 9. Conclusiones

Las variables de entorno te ayudan a:
- Mantener la seguridad de tus credenciales
- Separar la configuración de tu código
- Facilitar la transición entre ambientes de desarrollo, prueba y producción

Usar archivos `.env` con la librería `python-dotenv` es una forma sencilla y directa de lograrlo en Python. 

---

### Referencias y Recursos

- [Repositorio de python-dotenv en GitHub](https://github.com/theskumar/python-dotenv)
- [Documentación oficial de Python: os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

---
