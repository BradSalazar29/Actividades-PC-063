import getpass
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

correo_personal = input('ingresa tu correo: ')
contra = getpass.getpass(prompt='Cual es tu password: ')
correo_destino = input('ingrese el correo de destino: ')
asunto_correo = input('ingrese el asunto del correo: ')
cuerpo_correo = input('ingrese el cuerpo del correo')

imagen = input('ingree la ruta de la imagen')
imagen = imagen.replace("\\", '/')
imagen = imagen.replace('"', '')
nombre_completo = input('ingrse su nombre completo: ')

mensaje = MIMEMultipart()
mensaje["From"] = correo_personal
mensaje["To"] = correo_destino
mensaje["Subject"] = asunto_correo

mensaje.attach(MIMEText(nombre_completo+'\n'+cuerpo_correo, "plain"))


with open(imagen, "rb") as attachment:

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())


encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {imagen}",
)

mensaje.attach(part)
text = mensaje.as_string()


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(correo_personal, contra)
    server.sendmail(correo_personal, correo_destino, text)
