import socket

from cryptography.fernet import Fernet

key = Fernet.generate_key()

k = Fernet(key)

frase = input('ingrese la frase ')
with open('clave.key', 'wb') as archivio_clave:
    archivio_clave.write(key)
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# aqui conectamos con la ip y el puerto
sock.connect((TCP_IP, TCP_PORT))
# mandamos al servidor la frase en tipo bytes y encriptada
sock.send(k.encrypt(frase.encode()))

# aqui recibimos el mensaje

msgReceived = sock.recv(BUFFER_SIZE)

print(msgReceived.decode())
