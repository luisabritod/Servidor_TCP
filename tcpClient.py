import socket
import sys


HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados
BUFFER_RECEBE = BUFFER_SIZE + 1  # teste


def main(argv):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Servidor executando!")
            while(True):
                texto = input("Digite o texto a ser enviado ao servidor:\n")
                # texto.encode - converte a string para bytes
                s.send(texto.encode())
                data = s.recv(BUFFER_SIZE)
                # converte de bytes para um formato "printável"
                texto_recebido = repr(data)
                print('Recebido do servidor', texto_recebido)
                # txt = input(
                # '1-Saber a quantidade de vogais;\n2-Saber a quantidade de consoantes;\n3-Saber a palavra invertida;\n4-Todas as funções:\n')
                # print(vogais, consoantes, invertido)
                # converte os bytes em string
                texto_string = data.decode('utf-8')
                # vogais = data.decode('utf-8')
                if (texto_string == 'bye'):
                    print('vai encerrar o socket cliente!')
                    s.close()
                    break
    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":
    main(sys.argv[1:])
