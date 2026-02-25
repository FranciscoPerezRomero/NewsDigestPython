from dotenv import load_dotenv
import os

#* .env Variables - ruta absoluta desde la raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

#* Importamos las credenciales
NEWS_APIKEY = os.getenv("NEWS_APIKEY")
ANTHROPIC_APIKEY = os.getenv("ANTHROPIC_APIKEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

#* Validación de credenciales
if not NEWS_APIKEY or not ANTHROPIC_APIKEY or not EMAIL_SENDER or not EMAIL_PASSWORD:
    raise ValueError('Credentials not found')