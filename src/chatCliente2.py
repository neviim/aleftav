# -*- coding: utf-8 -*-' 
# chat_client.py

''' Cliente
    
    $ python chatCliente.py <ip_do_chatserver> 9009
    Conectado ao host remoto. Você pode começar a enviar mensagens
'''

import sys
import socket
import select
import os
from cores import *
 

def chat_client():
    if(len(sys.argv) < 3) :
        print 'Como utilizar: python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # conectar-se ao host remoto
    try :
        s.connect((host, port))
    except :
        print 'Incapaz de conectar'
        sys.exit()

    
    # limpar a tela
    if sys.platform == "linux" or sys.platform == "linux2":
        # linux
        os.system("clear")
    elif platform == "darwin":
        # OS X
    elif platform == "win32":
        #Windows
        os.system("cls")
    
    
    print CYAN+ ALEFTAV1 +NORMAL     
    print YELLOW + 'Systema conectado, modulo mensagem ativo!!! - V0.4 \n' + NORMAL 
    sys.stdout.write( RED +'[-->] '+ NORMAL ); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Obtenha os sockets da lista que são legíveis
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # mensagem recebida do servidor remoto, s
                data = sock.recv(4096)
                if not data :
                    print '\nDesconectado do servidor de bate-papo' 
                    sys.exit()
                else :
                    # escreve os dados
                    sys.stdout.write(data)
                    sys.stdout.write( GREEN + '[<--] ' + NORMAL ); sys.stdout.flush()     
            
            else :
                # usuário digitou uma mensagem
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write( GREEN + '[<--] ' + NORMAL ); sys.stdout.flush() 


if __name__ == "__main__":
    sys.exit(chat_client())