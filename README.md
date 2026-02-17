# NewsDigestPython

Aplicación en Python para obtener, procesar y enviar resúmenes de noticias personalizados por correo electrónico.

## Descripción

NewsDigest consume la API de [NewsAPI.org](https://newsapi.org/) para buscar artículos por temas definidos por el usuario, los procesa con IA (Anthropic) para generar resúmenes y los distribuye vía email.

## Estado actual

- **Configuración de credenciales** (`config/settings.py`) — carga y valida variables de entorno desde `.env`
- **Cliente de NewsAPI** (`api/news_client.py`) — consulta artículos por temas, idioma y país (por defecto: español/México)
- Módulos de base de datos, procesamiento, resumen por IA, envío de correo y scheduler están preparados como scaffolding

## Requisitos

- Python 3.11+
- Cuenta en [NewsAPI.org](https://newsapi.org/)
- Clave de API de Anthropic (pendiente de integración)

## Instalación

```bash
# Crear y activar entorno virtual
python -m venv venv
./venv/Scripts/activate  # Windows

# Instalar dependencias
pip install -r requeriments.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto:

```env
NEWS_APIKEY=tu_api_key_de_newsapi
ANTHROPIC_APIKEY=tu_api_key_de_anthropic
EMAIL_SENDER=tu_correo@ejemplo.com
```

## Estructura del proyecto

```
NewsDigest/
├── api/news_client.py        # Cliente para consumir NewsAPI
├── config/settings.py        # Carga de credenciales y configuración
├── db/database.py            # (pendiente) Persistencia de datos
├── models/user.py            # (pendiente) Modelo de usuario
├── services/
│   ├── mailer.py             # (pendiente) Envío de correos
│   ├── processor.py          # (pendiente) Procesamiento de noticias
│   └── summarizer.py         # (pendiente) Resumen con IA
├── main.py                   # (pendiente) Punto de entrada
└── scheduler.py              # (pendiente) Orquestador de tareas
```
