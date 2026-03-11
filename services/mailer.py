import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import EMAIL_SENDER , EMAIL_PASSWORD

def send_email(userName, userEmail, newsResume):
    server = None
    try:
        print(f"[DEBUG] Iniciando envío para {userEmail}")
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = userEmail
        msg['Subject'] = 'Tus noticias del día'
        
        print(f"[DEBUG] Construyendo HTML para {len(newsResume)} noticias")
        noticias_html = ""
        for article in newsResume:
            noticias_html += f"""
                <div style="margin-bottom: 20px;">
                    <h3>{article['title']}</h3>
                    <p>{article['summary']}</p>
                    <a href="{article['url']}">Leer más</a>
                </div>
            """
        
        body = f"""
        <html>
        <body>
            <h1>Hola {userName}!</h1>
            <p>Aquí están tus noticias del día:</p>
            {noticias_html}
        </body>
        </html>
        """
        
        print("[DEBUG] Adjuntando body al mensaje")
        msg.attach(MIMEText(body, 'html'))
        
        print("[DEBUG] Conectando a Gmail SMTP...")
        server = smtplib.SMTP('smtp.gmail.com', 465)
        server.starttls()
        
        print("[DEBUG] Haciendo login...")
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        
        print("[DEBUG] Enviando mensaje...")
        server.send_message(msg)
        
        print(f"[DEBUG] Email enviado exitosamente a {userEmail}")

    except Exception as e:
        print(f"[ERROR] Falló send_email: {type(e).__name__}: {str(e)}")
        return None
    finally:
        if server is not None:
            server.quit()