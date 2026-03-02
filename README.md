# NewsDigestPython

Aplicación en Python para obtener, procesar y enviar resúmenes de noticias personalizados por correo electrónico.

## Descripción

NewsDigest consume la API de [NewsAPI.org](https://newsapi.org/) para buscar artículos por temas definidos por el usuario, los deduplica por similitud de títulos (Jaccard), genera resúmenes con IA (Anthropic Claude) y los distribuye vía Gmail SMTP.

## Estado actual

- **Configuración de credenciales** (`config/settings.py`) — carga y valida variables de entorno desde `.env`
- **Cliente de NewsAPI** (`api/news_client.py`) — consulta artículos por temas con OR; por defecto español/México
- **Base de datos SQLite** (`db/database.py`) — tablas `users` y `user_tags`; funciones CRUD completas
- **Procesador de noticias** (`services/processor.py`) — deduplicación por similitud de títulos usando índice de Jaccard (≥50%)
- **Resumen con IA** (`services/summarizer.py`) — resúmenes de 2-3 líneas por artículo con Anthropic Claude; fallback a descripción original
- **Mailer** (`services/mailer.py`) — envío de correos HTML vía Gmail SMTP con contraseña de app
- **Punto de entrada** (`main.py`) — `send_daily_digest()`: flujo completo por usuario (tags → noticias → resumen → email)
- **Scheduler** (`scheduler.py`) — ejecuta `send_daily_digest()` automáticamente todos los días a las 6:00 AM
- **API REST con FastAPI** (`api.py`) — *(en desarrollo)* instancia de FastAPI con modelo `UserRegister` (Pydantic); endpoints pendientes de implementación

## Requisitos

- Python 3.11+
- Cuenta en [NewsAPI.org](https://newsapi.org/)
- Clave de API de Anthropic (con créditos activos)
- Cuenta de Gmail con contraseña de app habilitada

## Instalación

```bash
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS

# Instalar dependencias
pip install -r requeriments.txt

# Inicializar la base de datos (solo la primera vez)
python -c "from db.database import init_db; init_db()"
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto:

```env
NEWS_APIKEY=tu_api_key_de_newsapi
ANTHROPIC_APIKEY=tu_api_key_de_anthropic
EMAIL_SENDER=tu_correo@gmail.com
EMAIL_PASSWORD=tu_contraseña_de_app_gmail
```

## Uso

```bash
# Ejecutar el digest una sola vez
python -m main

# Ejecutar el scheduler (dispara automáticamente a las 6:00 AM)
python scheduler.py
```

> **Nota:** Siempre ejecutar desde la raíz del proyecto usando `python -m <modulo>`. Correr archivos directamente (`python services/summarizer.py`) causa errores de importación.

## Estructura del proyecto

```
NewsDigest/
├── api/news_client.py        # Cliente para consumir NewsAPI
├── config/settings.py        # Carga y validación de credenciales
├── db/database.py            # Base de datos SQLite (users, user_tags)
├── models/user.py            # (pendiente) Modelo de usuario
├── services/
│   ├── mailer.py             # Envío de correos HTML vía Gmail SMTP
│   ├── processor.py          # Deduplicación de noticias por similitud Jaccard
│   └── summarizer.py         # Resumen con IA vía Anthropic Claude
├── api.py                    # (en desarrollo) API REST con FastAPI
├── main.py                   # send_daily_digest(): flujo completo del digest
└── scheduler.py              # Orquestador: ejecuta digest diariamente a las 6:00 AM
```
