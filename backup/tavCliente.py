# -*- coding: utf-8 -*-
# ~/env/py36/bin/python

import socket

# cliente socket
def client_program():
    # ip e porta do servidor de mensagem.
    port = 5000    # porta socket server
    hostServer = ('192.168.200.213', port)

    client_socket = socket.socket()     # instantiate
    client_socket.connect(hostServer)   # connect to the server

    message = input(" -> ")

    while message.lower().strip() != 'tav':
        # envia menssagem para o server
        client_socket.send(message.encode("utf-8"))  
        # recebe mensagem do server
        data = client_socket.recv(1024).decode() 

        # mostra mensagem no terminal
        print('Received from server: ' + data)

        message = input(" -> ") 

    # fecha conecçao socket
    client_socket.close()  


if __name__ == '__main__':
    client_program()
