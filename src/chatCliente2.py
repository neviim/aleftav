# -*- coding: utf-8 -*-' 
# chat_client.py

''' Cliente
    
    $ python chat_client.py localhost 9009
     Conectado ao host remoto. Você pode começar a enviar mensagens
'''

import sys
import socket
import select
 
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
     
    print 'Conectado ao servidor. pode enviar mensagens' 
    sys.stdout.write('[-->] '); sys.stdout.flush()
     
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
                    sys.stdout.write('[<--] '); sys.stdout.flush()     
            
            else :
                # usuário digitou uma mensagem
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[<--] '); sys.stdout.flush() 


if __name__ == "__main__":
    sys.exit(chat_client())