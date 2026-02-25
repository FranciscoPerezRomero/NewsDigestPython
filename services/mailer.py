import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['FROM'] = 'plicdreft@gmail.com'
msg['TO'] = 'destino'
msg['Subject'] = 'asunto'


body = '<h1>Hola!</h1><p>Estructura de email</p>'
