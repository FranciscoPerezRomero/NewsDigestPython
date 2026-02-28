import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import EMAIL_SENDER , EMAIL_PASSWORD

def send_email(userName,userEmail,newsResume):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = userEmail
        msg['Subject'] = 'asunto'
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
        msg.attach(MIMEText(body,'html'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER,EMAIL_PASSWORD)
        server.send_message(msg)
    except Exception as e:
        return None
    finally:
        server.quit()