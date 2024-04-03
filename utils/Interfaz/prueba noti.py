import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Puerto para conexiones TLS

# Dirección de correo electrónico del remitente y destinatario
from_email = 'xitope3828@adstam.com'
to_email = 'tonovera3@gmail.com'

# Tu cuenta de Gmail y contraseña (debes habilitar el acceso de aplicaciones menos seguras en tu cuenta de Gmail)
gmail_username = 'xitope3828@adstam.com'
gmail_password = 'Hackaton2024'

# Crear el objeto del mensaje
message = MIMEMultipart()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = 'Asunto del correo'

# Contenido del correo
body = "Hola,\n\nEste es un correo de prueba enviado desde Python."

# Adjuntar el cuerpo del correo
message.attach(MIMEText(body, 'plain'))

# Iniciar conexión al servidor SMTP de Gmail
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Autenticarse en el servidor SMTP de Gmail
server.login(gmail_username, gmail_password)

# Enviar el correo electrónico
server.sendmail(from_email, to_email, message.as_string())

# Cerrar la conexión al servidor SMTP de Gmail
server.quit()

print('Correo enviado exitosamente.')
