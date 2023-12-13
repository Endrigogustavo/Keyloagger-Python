import socket

# Configurar o cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

while True:
    # Receber tecla do servidor
    tecla = client_socket.recv(1024).decode('utf-8')
    print('Tecla Recebida:', tecla)

# Fechar conexão (essa parte será alcançada somente quando a conexão for encerrada pelo servidor)
client_socket.close()
