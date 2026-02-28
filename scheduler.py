import schedule
import time
from main import send_daily_digest

#* Ejecución de funciones
def job(): 
    send_daily_digest()

#* Ejecución automatica
schedule.every().day.at("6:00").do(job)
# schedule.every(1).minutes.do(job)
print("Scheduler initialized waiting for the time to start")
print("Ctrl + C to stop")

#* Loop infinito para evaluar
while True:
    schedule.run_pending()
    time.sleep(60) #? Esto repite cada 60 segundos