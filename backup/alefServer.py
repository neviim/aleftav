# -*- coding: utf-8 -*-
# ~/env/py36/bin/python

import socket

def server_program():
    port = 5000 # conecta acima de 1024
    hostServer = ('0.0.0.0', port)

    server_socket = socket.socket()  # obter instância
    server_socket.bind(hostServer)   # vincular endereço de host e porta juntos

    # escutar simultaneamente 
    server_socket.listen(2) # (2) clientes
    conn, address = server_socket.accept()  
    print("Conectado em: " + str(address))

    while True:
        # receber fluxo de dados. não aceita pacote maior que 1024 bytes
        data = conn.recv(1024).decode("utf-8")
        if not data:
            # se os dados não forem recebidos
            break

        print("do usuário conectado: " + str(data))
        data = input(' -> ')

        # enviar dados para o cliente
        conn.send(data.encode())

    conn.close() 


if __name__ == '__main__':
    server_program()
