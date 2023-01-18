import socket
import sys
from threading import Thread
from unicodedata import normalize

HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados
# BUFFER_RECEBE = BUFFER_SIZE + 1  # teste


def on_new_client(clientsocket, addr):
    while True:
        try:
            data = clientsocket.recv(BUFFER_SIZE)
            if not data:
                break
            # converte os bytes em string
            texto_recebido = data.decode('utf-8')
            print('recebido do cliente {} na porta {}: {}'.format(
                addr[0], addr[1], texto_recebido))
            # envia o mesmo texto ao cliente
            vogais, consoantes, invertido = retorno(texto_recebido)
            # print(vogais, consoantes, invertido)
            clientsocket.send(data)
            # olhar clientsocket.write
            if (texto_recebido == 'bye'):
                print('vai encerrar o socket do cliente {} !'.format(addr[0]))
                clientsocket.close()
                return
        except Exception as error:
            print("Erro na conexão com o cliente!!")
            return


def main(argv):
    try:
        # AF_INET: indica o protocolo IPv4. SOCK_STREAM: tipo de socket para TCP,
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            while True:
                server_socket.listen()
                clientsocket, addr = server_socket.accept()
                print('Conectado ao cliente no endereço:', addr)
                t = Thread(target=on_new_client, args=(clientsocket, addr))
                t.start()
    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)
        return

# função retorna o solicitado pelo professor


def retorno(recebe):
    # recebe é variavel com a string enviada pelo cliente
    vogais = 0
    consoantes = 0

    for i in range(len(recebe)):
        letra = recebe[i]
        letra = normalize('NFD', letra)[0].lower()
        # utilizei a função normalize para generalizar todas as letras para letras minusculas e sem acentuação
        if letra in ('a', 'e', 'i', 'o', 'u'):
            vogais = vogais+1
        elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
            consoantes = consoantes+1

    # print('vogais: ', vogais)
    # print('consoantes: ', consoantes)

    # print('invertido: ', recebe[::-1])
    invertido = recebe[::-1]
    return vogais, consoantes, invertido


if __name__ == "__main__":
    main(sys.argv[1:])
