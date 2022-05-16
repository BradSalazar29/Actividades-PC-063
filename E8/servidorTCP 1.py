import socket
from cryptography.fernet import Fernet

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen()

(clientSocket, clientAddress) = sock.accept()

while True:

    data = clientSocket.recv(BUFFER_SIZE)

    if data != b'':

        palabra = 'entereado bye'

        clientSocket.send(palabra.encode())

        break
with open('clave.key', 'rb') as archivo_clave:
    llave = archivo_clave.read()

key = llave
k = Fernet(key)

mensaje_final = k.decrypt(data)
print(mensaje_final.decode())
