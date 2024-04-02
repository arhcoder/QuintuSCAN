import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Datos del remitente
email = 'anomaliquintusbot@gmail.com'
password = 'Hackaton2024'

# Datos del destinatario
to_email = 'tonovera3@gmail.com'

# Configurar el mensaje
subject = 'Prueba'
body = 'Hola esta es una prueba de correo'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Iniciar sesión en el servidor SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

# Enviar correo electrónico
server.sendmail(email, to_email, msg.as_string())

# Cerrar conexión
server.quit()
