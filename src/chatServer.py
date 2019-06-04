# -*- coding: utf-8 -*-' 
# chat_server.py
 
''' Server

    $ python chat_server.py
    Servidor de bate-papo iniciado na porta 9009    
'''

import sys
sys.path.append('../color')

import socket
import select
from cores import *

HOST = '192.168.200.213' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # adicionar objeto de socket do servidor à lista de conexões legíveis
    SOCKET_LIST.append(server_socket)
 
    print CYAN+ ALEFTAV1 +NORMAL
    print "Serviço ativo, inicializado na porta: " + YELLOW + str(PORT) + NORMAL + '\n'

 
    while 1:

        # obter os sockets de lista que estão prontos para serem lidos através de select
        # 4th arg, time_out = 0: pesquisa e nunca bloqueia
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # um novo pedido de conexão recebido
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Cliente (%s:%s) conectado" % addr
                 
                broadcast(server_socket, sockfd, "[%s:%s] entrou na nossa sala de chat\n" % addr)
             
            # uma mensagem de um cliente, não uma nova conexão
            else:
                try:
                    # dados do processo recebidos do cliente.
                    data = sock.recv(RECV_BUFFER)

                    if data:
                        # há algo no socket
                        hostIp, userId = str(sock.getpeername())
                        broadcast(server_socket, sock, "\r" + GREEN + "[<--] " + NORMAL + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        # remova o socket que está quebrado    
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # nesta fase, nenhum dado significa que provavelmente a conexão foi interrompida
                        broadcast(server_socket, sock, "Cliente (%s, %s) está offline\n" % addr) 

                # exceção 
                except:
                    broadcast(server_socket, sock, "Usuario (%s, %s) está offline\n" % addr)
                    continue

    server_socket.close()
    
# Envia a mensagens de chat para todos os usuarios conectados
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # enviar a mensagem apenas para peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # conexão de socket quebrada
                socket.close()
                # socket quebrado, remova-o
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)


if __name__ == "__main__":
    sys.exit(chat_server()) 